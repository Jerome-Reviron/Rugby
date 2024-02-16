import pandas as pd
from app.models import Player, Club, D_CLUB, D_AGEGRP, D_DATE, D_ETABLISHEMENT, D_SEX, F_PLAYER
from django.db import transaction

global_counter = 0

def run():
    # # Charger les DataFrames à partir de la base de données
    df_club_apres_bulk_create = pd.DataFrame.from_records(D_CLUB.objects.values())
    # print("Colonnes de df_club_apres_bulk_create:", df_club_apres_bulk_create.columns)


    # Liste pour stocker les objets F_PLAYER
    f_player_objects = []
    total_rows = len(f_player_objects)

    # Charger les DataFrames pour Player et Club
    player_data = Player.objects.filter(region="Auvergne-Rhône-Alpes").values()
    df_player = pd.DataFrame.from_records(player_data)
    # print("Colonnes de df_player:", df_player.columns)

    club_data = Club.objects.filter(region="Auvergne-Rhône-Alpes").values()
    df_club = pd.DataFrame.from_records(club_data)
    # print("Colonnes de df_club:", df_club.columns)
    
    # Fusionner les DataFrames pour créer le big_dataframe
    big_dataframe = pd.merge(df_player, df_club, on=["code", "code_qpv", "code_commune"])
    # Convertir la colonne 'code' de df_club_apres_bulk_create en type objet
    df_club_apres_bulk_create['code'] = df_club_apres_bulk_create['code'].astype(str)
    big_dataframe = pd.merge(big_dataframe, df_club_apres_bulk_create, how='left', on=["code", "code_qpv", "code_commune"])
    # print("Colonnes de big_dataframe:", big_dataframe.columns)

    # Appliquer le filtre sur la colonne 'code_commune'
    big_dataframe = big_dataframe.loc[big_dataframe['code_commune'] != "NR - Non réparti"]
    # print("Colonnes de big_dataframe:", big_dataframe.columns)

    # Fusionner les colonnes "club" et "epa"
    big_dataframe['etablishementlabel'] = big_dataframe.apply(get_etablishment_label, axis=1)
    big_dataframe['nombre'] = big_dataframe.apply(get_nombre_value, axis=1)
    big_dataframe['etablishement_id'] = big_dataframe.apply(lambda row: get_etablishment_id(row, global_counter), axis=1)
    # print("Colonnes de big_dataframe:", big_dataframe.columns)

    # Colonnes à fondre (melt)
    melt_columns = ["f_1_4_ans", "f_5_9_ans", "f_10_14_ans", "f_15_19_ans", "f_20_24_ans", "f_25_29_ans",
                    "f_30_34_ans", "f_35_39_ans", "f_40_44_ans", "f_45_49_ans", "f_50_54_ans", "f_55_59_ans",
                    "f_60_64_ans", "f_65_69_ans", "f_70_74_ans", "f_75_79_ans", "f_80_99_ans", "f_nr",
                    "h_1_4_ans", "h_5_9_ans", "h_10_14_ans", "h_15_19_ans", "h_20_24_ans", "h_25_29_ans",
                    "h_30_34_ans", "h_35_39_ans", "h_40_44_ans", "h_45_49_ans", "h_50_54_ans", "h_55_59_ans",
                    "h_60_64_ans", "h_65_69_ans", "h_70_74_ans", "h_75_79_ans", "h_80_99_ans", "h_nr", "nr_nr"]

    # Effectuer la fusion (melt) des colonnes spécifiées
    melted_dataframe = pd.melt(big_dataframe, id_vars=['code_code_qpv_code_commune', "code", "code_qpv", "code_commune", 'etablishement_id', 'date'], value_vars=melt_columns, var_name="category", value_name="value")

    # Créer une colonne 'sexcode' à partir du nom de la colonne 'category'
    melted_dataframe['sexcode'] = melted_dataframe['category'].apply(get_sex_code)

    # Créer une colonne 'agegrplabel' à partir du nom de la colonne 'category'
    melted_dataframe['agegrplabel'] = melted_dataframe['category'].apply(get_agegrp_label)
    # print("Colonnes de melted_dataframe:", melted_dataframe.columns)

    # Utiliser une transaction atomique pour garantir l'intégrité de la base de données
    with transaction.atomic():
        total_rows_inserted = 0
        try:
            # Itérer sur les lignes de melted_dataframe
            for _, row in melted_dataframe.iterrows():
                # Créer des instances de D_CLUB, D_AGEGRP, D_DATE, D_ETABLISHEMENT, D_SEX
                d_club_instance = D_CLUB(
                    code_code_qpv_code_commune=row['code_code_qpv_code_commune']
                )
                d_etablishement_instance = D_ETABLISHEMENT(
                    etablishement_id=row['etablishement_id']
                )
                d_sex_instance = D_SEX(
                    sexcode=row['sexcode']
                )
                d_agegrp_instance = D_AGEGRP(
                    agegrplabel=row['agegrplabel']
                )
                d_date_instance = D_DATE(
                    date=row['date']
                )
                d_club_instance = D_CLUB(
                    code=row['code'],
                    code_qpv=row['code_qpv'],
                    code_commune=row['code_commune'],
                )
                
                # Enregistrez les instances de D_CLUB, D_AGEGRP, D_DATE, D_ETABLISHEMENT, D_SEX
                d_club_instance.save()
                d_etablishement_instance.save()
                d_sex_instance.save()
                d_agegrp_instance.save()
                d_date_instance.save()
                d_club_instance.save()

                # Créer l'objet F_PLAYER avec les relations correctement sauvegardées
                f_player_instance = F_PLAYER(
                    D_CLUB_FK=d_club_instance,
                    D_ETABLISHEMENT_FK=d_etablishement_instance,
                    D_SEX_FK=d_sex_instance,
                    D_AGEGRP_FK=d_agegrp_instance,
                    D_DATE_FK=d_date_instance,
                )

                f_player_objects.append(f_player_instance)

                # Mettre à jour le nombre total de lignes insérées
                total_rows_inserted += 1

                # Afficher un message à chaque itération
                if total_rows_inserted % 1000 == 0:
                    print(f"{total_rows_inserted} lignes insérées...")

            # Afficher le nombre total de lignes qui seront insérées
            print(f"Nombre total de lignes à insérer : {total_rows_inserted}")

            chunk_size = 10000

            # # Utilisation de bulk_create avec ignore_conflicts=True
            # F_PLAYER.objects.bulk_create(f_player_objects, ignore_conflicts=True)

            for i in range(0, len(f_player_objects), chunk_size):
                chunk = f_player_objects[i:i + chunk_size]
                F_PLAYER.objects.bulk_create(chunk)
                print("Chunk inséré avec succès!")
            print(f"Script terminé avec succès! {len(f_player_objects)} lignes insérées.")
        except Exception as e:
            print(f"Une erreur s'est produite pendant l'insertion : {str(e)}")
            
def get_etablishment_label(row):
    clubs = int(row['clubs']) if 'clubs' in row else 0
    epa = int(row['epa']) if 'epa' in row else 0

    if clubs > 0 and epa > 0:
        return f"clubs/epa"
    elif clubs > 0:
        return f"clubs"
    elif epa > 0:
        return f"epa"
    else:
        return "unknown"

def get_nombre_value(row):
    clubs = int(row['clubs']) if 'clubs' in row else 0
    epa = int(row['epa']) if 'epa' in row else 0

    if clubs > 0 and epa > 0:
        return f"{clubs};{epa}"
    elif clubs > 0:
        return str(clubs)
    elif epa > 0:
        return str(epa)
    else:
        return "unknown"

def get_etablishment_id(row, counter):
    global global_counter
    result = f"{counter}-{row['etablishementlabel']}-{row['nombre']}"
    global_counter += 1
    return result

def get_sex_code(column):
    # Logique pour extraire le code de sexe à partir des noms de colonnes
    if 'f' in column.lower():
        return 'f'
    elif 'h' in column.lower():
        return 'h'
    elif 'nr' in column.lower():
        return 'nr'
    else:
        return None

def get_agegrp_label(column):
    # Logique pour extraire la partie après le premier '_' et avant 'ans' dans le nom de la colonne
    parts = column.split('_')
    if len(parts) > 1 and parts[-1] == 'ans':
        return f"_{parts[1]}_{parts[2]}_{parts[3]}_ans"
    else:
        return None

if __name__ == "__main__":
    run()
