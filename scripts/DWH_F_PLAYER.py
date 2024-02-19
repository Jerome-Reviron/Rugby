import pandas as pd
from app.models import Player, Club, D_CLUB, D_AGEGRP, D_DATE, D_ETABLISHEMENT, D_SEX, F_PLAYER
from django.db import transaction

global_counter = 0

def run():

    # Liste pour stocker les objets F_PLAYER
    f_player_objects = []
    total_rows = len(f_player_objects)

    # Charger les DataFrames pour Player et Club
    player_data = Player.objects.filter(region="Auvergne-Rhône-Alpes").values()
    df_player = pd.DataFrame.from_records(player_data)
    # print(df_player.head())

    club_data = Club.objects.filter(region="Auvergne-Rhône-Alpes").values()
    df_club = pd.DataFrame.from_records(club_data)
    # print(df_club.head())

    # # Charger les DataFrames à partir de la base de données
    df_club_apres_bulk_create = pd.DataFrame.from_records(D_CLUB.objects.values())
    # print(df_club_apres_bulk_create.columns)
    # print(df_club_apres_bulk_create.head())

    # Fusionner les DataFrames pour créer le big_dataframe
    big_dataframe = pd.merge(df_player, df_club, on=["code", "code_qpv", "code_commune", "nom_qpv",
                                                    "federation", "region", "departement",
                                                    "code_commune", "commune", "statut_geo"])
    # print(big_dataframe.columns)
    # print(big_dataframe.head())

    # Convertir la colonne 'code' de df_club_apres_bulk_create en type objet
    df_club_apres_bulk_create['code'] = df_club_apres_bulk_create['code'].astype(str)
    big_dataframe = pd.merge(big_dataframe, df_club_apres_bulk_create, how='left',
                                                    on=["code", "code_qpv", "code_commune", "nom_qpv",
                                                    "federation", "region", "departement",
                                                    "commune", "statut_geo"])
    # print(big_dataframe.columns)
    # print(big_dataframe.head())

    # Appliquer le filtre sur la colonne 'code_commune'
    big_dataframe = big_dataframe.loc[big_dataframe['code_commune'] != "NR - Non réparti"]

    # Colonnes à fondre (sexcode/agegrplabel)
    melt_columns_1 = ["f_1_4_ans", "f_5_9_ans", "f_10_14_ans", "f_15_19_ans", "f_20_24_ans", "f_25_29_ans",
                    "f_30_34_ans", "f_35_39_ans", "f_40_44_ans", "f_45_49_ans", "f_50_54_ans", "f_55_59_ans",
                    "f_60_64_ans", "f_65_69_ans", "f_70_74_ans", "f_75_79_ans", "f_80_99_ans",
                    "h_1_4_ans", "h_5_9_ans", "h_10_14_ans", "h_15_19_ans", "h_20_24_ans", "h_25_29_ans",
                    "h_30_34_ans", "h_35_39_ans", "h_40_44_ans", "h_45_49_ans", "h_50_54_ans", "h_55_59_ans",
                    "h_60_64_ans", "h_65_69_ans", "h_70_74_ans", "h_75_79_ans", "h_80_99_ans"]

    # Effectuer la fusion des colonnes spécifiées
    melted_dataframe_1 = pd.melt(big_dataframe, id_vars=["code_code_qpv_code_commune", "code", "code_qpv", "code_commune",
                                                        "nom_qpv", "federation", "region", "departement",
                                                        "commune", "statut_geo", "date"],
                            value_vars=melt_columns_1,
                            var_name="category_MC_1",
                            value_name="value_MC_1")
    # print(melted_dataframe_1['category_MC_1'].unique())

    melted_dataframe_1['sexcode'] = melted_dataframe_1['category_MC_1'].apply(get_sex_code)
    melted_dataframe_1['agegrplabel'] = melted_dataframe_1['category_MC_1'].apply(get_agegrp_label)
    melted_dataframe_1 = melted_dataframe_1.loc[(melted_dataframe_1['sexcode'] != 'nr') & (melted_dataframe_1['value_MC_1'].notna())]
    melted_dataframe_1 = melted_dataframe_1.loc[(melted_dataframe_1['agegrplabel'].notna()) & (melted_dataframe_1['value_MC_1'].notna())]
    # print(melted_dataframe_1.head())

    # Effectuer la fusion des colonnes spécifiées
    melt_columns_2 = ["clubs", "epa"]
    melted_dataframe_2 = pd.melt(big_dataframe, id_vars=["code_code_qpv_code_commune", "code", "code_qpv", "code_commune",
                                                        "nom_qpv", "federation", "region", "departement",
                                                        "commune", "statut_geo", "date"],
                                value_vars=melt_columns_2,
                                var_name="category_MC_2",
                                value_name="value_MC_2")

    # Créer une colonne 'etablishementlabel' à partir du nom de la colonne 'category'
    melted_dataframe_2['etablishementlabel'] = melted_dataframe_2['category_MC_2'].apply(get_etablishement_label)
    melted_dataframe_2['nombre'] = melted_dataframe_2['value_MC_2']
    melted_dataframe_2 = melted_dataframe_2.loc[(melted_dataframe_2['etablishementlabel'] != '')]
    melted_dataframe_2 = melted_dataframe_2.loc[(melted_dataframe_2['nombre'] != 0)]
    # print(melted_dataframe_2.head())

    # Fusionner melted_dataframe_1 avec big_dataframe
    merged_dataframe_1 = pd.merge(big_dataframe, melted_dataframe_1,
                                                        on=["code_code_qpv_code_commune", "code", "code_qpv", "code_commune",
                                                        "nom_qpv", "federation", "region", "departement",
                                                        "commune", "statut_geo", "date"])

    # Fusionner melted_dataframe_2 avec big_dataframe
    merged_dataframe_2 = pd.merge(big_dataframe, melted_dataframe_2,
                                                        on=["code_code_qpv_code_commune", "code", "code_qpv", "code_commune",
                                                        "nom_qpv", "federation", "region", "departement",
                                                        "commune", "statut_geo", "date"])

    # Sélectionner les colonnes nécessaires dans le bon ordre
    final_dataframe = pd.concat([
        merged_dataframe_1[['code_code_qpv_code_commune', 'code', 'code_qpv',
                        'code_commune', 'nom_qpv', 'commune', 'sexcode', 'agegrplabel',
                        'federation', 'region', 'departement', 'statut_geo', 'date']],
        merged_dataframe_2[['etablishementlabel', 'nombre']]
    ], axis=1)
    # print(final_dataframe.head())

    # Liste pour stocker les objets F_PLAYER
    f_player_objects = []
    total_rows = len(f_player_objects)

    # Supprimer toutes les entrées existantes dans la table F_PLAYER
    F_PLAYER.objects.all().delete()

    # Utiliser une transaction atomique pour garantir l'intégrité de la base de données
    with transaction.atomic():
        total_rows_inserted = 0
        try:
            # Itérer sur les lignes de final_dataframe
            for _, row in final_dataframe.iterrows():
                # Créer des instances de D_CLUB, D_AGEGRP, D_DATE, D_ETABLISHEMENT, D_SEX
                d_club_instance = D_CLUB(
                    code_code_qpv_code_commune=row['code_code_qpv_code_commune'],
                    code=row['code'],
                    code_qpv=row['code_qpv'],
                    nom_qpv=row['nom_qpv'],
                    federation=row['federation'],
                    region=row['region'],
                    departement=row['departement'],
                    code_commune=row['code_commune'],
                    commune=row['commune'],
                    statut_geo=row['statut_geo'],
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
                d_etablishement_instance = D_ETABLISHEMENT(
                    etablishementlabel=row['etablishementlabel']
                )

                # Enregistrez les instances de D_CLUB, D_AGEGRP, D_DATE, D_ETABLISHEMENT, D_SEX
                d_club_instance.save()
                d_sex_instance.save()
                d_agegrp_instance.save()
                d_date_instance.save()
                d_etablishement_instance.save()

                # Créer la clé primaire concaténée
                D_5_PK = f"{row['code_code_qpv_code_commune']}_{row['date']}_{row['etablishementlabel']}_{row['sexcode']}_{row['agegrplabel']}"

                # Créer l'objet F_PLAYER avec les relations correctement sauvegardées
                f_player_instance = F_PLAYER(
                    D_5_PK,
                    D_CLUB_FK=d_club_instance,
                    D_SEX_FK=d_sex_instance,
                    D_AGEGRP_FK=d_agegrp_instance,
                    D_DATE_FK=d_date_instance,
                    D_ETABLISHEMENT_FK=d_etablishement_instance,
                    nombre=row['nombre']
                )

                f_player_objects.append(f_player_instance)

                # Mettre à jour le nombre total de lignes insérées
                total_rows_inserted += 1

                # Afficher un message à chaque itération
                if total_rows_inserted % 1000 == 0:
                    print(f"{total_rows_inserted} lignes insérées...")

            # Afficher le nombre total de lignes qui seront insérées
            print(f"Nombre total de lignes à insérer : {total_rows_inserted}")

            # Utilisation de bulk_create avec ignore_conflicts=True
            F_PLAYER.objects.bulk_create(f_player_objects, ignore_conflicts=True)

            # Stocker le DataFrame dans une variable
            df_f_player_apres_bulk_create = pd.DataFrame.from_records(F_PLAYER.objects.values())
            # print("Colonnes de df_sex_apres_bulk_create:", df_sex_apres_bulk_create.columns)

            print(f"Script terminé avec succès! {total_rows_inserted} lignes insérées.")
        except Exception as e:
            print(f"Une erreur s'est produite pendant l'insertion : {str(e)}")

def get_etablishement_label(column):
    if 'clubs' in column.lower():
        return 'clubs'
    elif 'epa' in column.lower():
        return 'epa'
    else:
        return ''

def get_sex_code(column):
    if 'f' in column.lower():
        return 'f'
    elif 'h' in column.lower():
        return 'h'
    elif 'nr' in column.lower():
        return 'nr'
    else:
        return None

def get_agegrp_label(column):
    parts = column.split('_')
    if len(parts) > 1 and parts[-1] == 'ans':
        return f"_{parts[1]}_{parts[2]}_{parts[3]}"
    else:
        return None

if __name__ == "__main__":
    run()
