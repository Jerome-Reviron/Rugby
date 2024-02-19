import pandas as pd
import os
from app.models import Player, Club, D_CLUB, D_AGEGRP, D_DATE, D_ETABLISHEMENT, D_SEX, F_PLAYER
from datetime import date
from django.db import IntegrityError
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

    # Fusionner les dataframes sur les colonnes communes
    common_columns = ['code_commune', 'commune', 'code_qpv', 'nom_qpv', 'departement', 'region', 'statut_geo', 'code', 'federation']
    df_fact = pd.merge(df_player, df_club, on=common_columns)

    # Filtrer les données
    df_fact = df_fact.query('region == "Auvergne-Rhône-Alpes" and commune != "NR - Non réparti"')

    # Supprimer les colonnes spécifiées
    df_fact = df_fact.drop(columns=["f_nr", "h_nr", "nr_nr", "total_x", "total_y"])

    # Colonnes à fondre (sexcode/agegrplabel)
    melt_columns_1 = ["f_1_4_ans", "f_5_9_ans", "f_10_14_ans", "f_15_19_ans", "f_20_24_ans", "f_25_29_ans",
                    "f_30_34_ans", "f_35_39_ans", "f_40_44_ans", "f_45_49_ans", "f_50_54_ans", "f_55_59_ans",
                    "f_60_64_ans", "f_65_69_ans", "f_70_74_ans", "f_75_79_ans", "f_80_99_ans",
                    "h_1_4_ans", "h_5_9_ans", "h_10_14_ans", "h_15_19_ans", "h_20_24_ans", "h_25_29_ans",
                    "h_30_34_ans", "h_35_39_ans", "h_40_44_ans", "h_45_49_ans", "h_50_54_ans", "h_55_59_ans",
                    "h_60_64_ans", "h_65_69_ans", "h_70_74_ans", "h_75_79_ans", "h_80_99_ans"]

    # Effectuer la fusion des colonnes spécifiées
    melted_dataframe_1 = pd.melt(df_fact, id_vars=[ "code", "code_qpv", "code_commune",
                                                    "nom_qpv", "federation", "region", "departement",
                                                    "commune", "statut_geo", "date"],
                            value_vars=melt_columns_1,
                            var_name="category_MC_1",
                            value_name="value_MC_1")

    melted_dataframe_1['sexcode'] = melted_dataframe_1['category_MC_1'].apply(get_sex_code)
    melted_dataframe_1['agegrplabel'] = melted_dataframe_1['category_MC_1'].apply(get_agegrp_label)
    melted_dataframe_1 = melted_dataframe_1.loc[(melted_dataframe_1['sexcode'].notna()) & (melted_dataframe_1['value_MC_1'].notna())]
    melted_dataframe_1 = melted_dataframe_1.loc[(melted_dataframe_1['agegrplabel'].notna()) & (melted_dataframe_1['value_MC_1'].notna())]

    # Bulk create D_SEX records, handling possible duplicates
    with transaction.atomic():
        try:
            # Créer une liste unique de noms de colonnes
            unique_columns = set()
            for column in melted_dataframe_1['category_MC_1'].unique():
                # Extraire le code de sexe (F, H, NR) à partir des noms de colonnes
                sex_code = get_sex_code(column)
                if sex_code and sex_code != 'nr' and sex_code != '':
                    unique_columns.add(sex_code)

            # Supprimer toutes les données de la table D_SEX avec le code 'nr' avant l'insertion
            D_SEX.objects.all().delete()
            print("Anciennes données effacées avant insertion!")

            # Utiliser bulk_create pour insérer les objets D_SEX en une seule requête
            D_SEX.objects.bulk_create([
                D_SEX(
                    sexcode=sex_code
                )
                for sex_code in unique_columns
            ])

            # Stocker le DataFrame dans une variable
            df_sex_apres_bulk_create = pd.DataFrame.from_records(D_SEX.objects.values())
            # print("Colonnes de df_sex_apres_bulk_create:", df_sex_apres_bulk_create.columns)

            print("Script D_SEX terminé avec succès!")
        except IntegrityError as e:
            print(f"Erreur lors de l'insertion des données : {e}")

    # Bulk create D_AGEGRP records, handling possible duplicates
    with transaction.atomic():
        try:
            # Créer une liste unique de noms de colonnes
            unique_columns = set()
            for column in melted_dataframe_1['category_MC_1'].unique():
                # Extraire le label d'âge à partir des noms de colonnes
                agegrp_label = get_agegrp_label(column)
                if agegrp_label and agegrp_label != 'nr':
                    unique_columns.add(agegrp_label)

            # Trier les labels d'âge uniquement sur la partie '20', '25', '30', ...
            sorted_age_labels = sorted(unique_columns, key=lambda x: int(x.split('_')[1]))

            # Supprimer toutes les données de la table D_AGEGRP avant l'insertion
            D_AGEGRP.objects.all().delete()
            print("Anciennes données effacées avant insertion!")

            # Utiliser bulk_create pour insérer les objets D_AGEGRP en une seule requête
            D_AGEGRP.objects.bulk_create([
                D_AGEGRP(
                    agegrplabel=agegrp_label
                )
                for agegrp_label in sorted_age_labels
            ])

            # Stocker le DataFrame dans une variable
            df_agegrp_apres_bulk_create = pd.DataFrame.from_records(D_AGEGRP.objects.values())
            # print("Colonnes de df_agegrp_apres_bulk_create:", df_agegrp_apres_bulk_create.columns)

            print("Script D_AGEGRP terminé avec succès!")
        except IntegrityError as e:
            print(f"Erreur lors de l'insertion des données : {e}")

    # Colonnes à fondre (etablishementlabel/nombre)
    melt_columns_2 = ["clubs", "epa"]

    # Effectuer la fusion des colonnes spécifiées pour les établissements
    melted_dataframe_2 = pd.melt(df_fact, id_vars=["code", "code_qpv", "code_commune",
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

    # Bulk create D_ETABLISHEMENT records, handling possible duplicates
    with transaction.atomic():
        try:
            # Créer une liste unique de noms de colonnes pour les établissements
            unique_etablishments = set(melted_dataframe_2['etablishementlabel'].unique())

            # Supprimer toutes les données de la table D_ETABLISHEMENT avant l'insertion
            D_ETABLISHEMENT.objects.all().delete()

            # Utiliser bulk_create pour insérer les objets D_ETABLISHEMENT en une seule requête
            D_ETABLISHEMENT.objects.bulk_create([
                D_ETABLISHEMENT(
                    etablishementlabel=etablishment
                )
                for etablishment in unique_etablishments
            ])

            # Afficher un message de succès
            print("Script D_ETABLISHEMENT terminé avec succès!")
        except IntegrityError as e:
            print(f"Erreur lors de l'insertion des données : {e}")

    # Bulk create D_DATE records, handling possible duplicates
    with transaction.atomic():
        try:
            # Récupérez l'année à partir des noms des fichiers CSV dans le dossier "data"
            years = find_unique_years('data')

            if years:
                # Supprimez toutes les données de la table D_DATE avant l'insertion
                D_DATE.objects.all().delete()
                print("Anciennes données effacées avant insertion!")

                # Utilisez bulk_create pour insérer l'objet D_DATE en une seule requête pour chaque année
                D_DATE.objects.bulk_create([
                    D_DATE(
                        date=date(year, 1, 1)  # Utilisez date() pour créer un objet date
                    )
                    for year in years
                ])

                # Stocker le DataFrame dans une variable
                df_date_apres_bulk_create = pd.DataFrame.from_records(D_DATE.objects.values())

                print("Script D_DATE terminé avec succès!")
        except IntegrityError as e:
            print(f"Erreur lors de l'insertion des données : {e}")

    # Bulk create D_CLUB records, handling possible duplicates
    with transaction.atomic():
        # Tri du DataFrame selon les colonnes spécifiées
        df_club_sorted = df_club.sort_values(by=['code', 'code_qpv', 'code_commune'])
        # print("Colonnes de df_club:", df_club.columns)

        try:
            # Supprimer toutes les données de la table D_CLUB avant l'insertion
            D_CLUB.objects.all().delete()
            print("Anciennes données effacées avant insertion!")

            for _, row in df_club_sorted.iterrows():
                key = f"{row['code']}-{row['code_qpv']}-{row['code_commune']}"
                D_CLUB.objects.update_or_create(
                    code_code_qpv_code_commune=key,
                    defaults={
                        'code': row['code'],
                        'code_qpv': row['code_qpv'],
                        'nom_qpv': row['nom_qpv'],
                        'federation': row['federation'],
                        'region': row['region'],
                        'departement': row['departement'],
                        'code_commune': row['code_commune'],
                        'commune': row['commune'],
                        'statut_geo': row['statut_geo'],
                    }
                )

            # Stocker le DataFrame dans une variable
            df_club_apres_bulk_create = pd.DataFrame.from_records(D_CLUB.objects.values())

            print("Script D_CLUB terminé avec succès!")
        except IntegrityError as e:
            print(f"Erreur lors de l'insertion des données : {e}")

def find_unique_years(data_folder):
    # Trouver tous les fichiers CSV dans le dossier spécifié
    csv_files = [file for file in os.listdir(data_folder) if file.endswith(".csv")]

    # Extraire les années uniques des noms des fichiers CSV
    unique_years = set()
    for csv_file in csv_files:
        year = get_year_from_csv(csv_file)
        if year is not None:
            unique_years.add(year)

    return list(unique_years)

def get_year_from_csv(csv_file):
    # Extraire l'année du nom du fichier CSV
    year = None
    file_name, file_ext = os.path.splitext(csv_file)
    parts = file_name.split("-")
    for part in parts:
        if part.isdigit() and len(part) == 4:
            year = int(part)
            break

    if year:
        print(f"Année extraite pour {csv_file}: {year}")
        return year
    else:
        print(f"Impossible d'extraire l'année pour {csv_file}")
        return None

def get_sex_code(column):
    if 'f' in column.lower():
        return 'f'
    elif 'h' in column.lower():
        return 'h'
    elif 'nr' in column.lower():
        return 'nr'

def get_agegrp_label(column):
    parts = column.split('_')
    if len(parts) > 1 and parts[-1] == 'ans':
        return f"{parts[1]}_{parts[2]}_{parts[3]}"
    else:
        return None

def get_etablishement_label(column):
    if 'clubs' in column.lower():
        return 'clubs'
    elif 'epa' in column.lower():
        return 'epa'
    else:
        return ''

if __name__ == "__main__":
    run()
