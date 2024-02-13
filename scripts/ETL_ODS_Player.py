import pandas as pd
from django.db import IntegrityError
from app.models import Player

def run():
    print("Chargement du fichier CSV...")
    # Charger le fichier CSV dans un DataFrame Pandas
    df = pd.read_csv("data/lic-data-2021.csv", delimiter=";", dtype=str)

    print(f"Nombre de lignes à insérer : {len(df)}")

    try:
        # Dictionnaire de correspondance entre les noms de colonnes et les attributs de Player
        column_mapping = {
            'Code Commune': 'code_commune',
            'Commune': 'commune',
            'Code QPV': 'code_qpv',
            'Nom QPV': 'nom_qpv',
            'Département': 'departement',
            'Région': 'region',
            'Statut géo': 'statut_geo',
            'Code': 'code',
            'Fédération': 'federation',
            'F - 1 à 4 ans': 'f_1_4_ans',
            'F - 5 à 9 ans': 'f_5_9_ans',
            'F - 10 à 14 ans': 'f_10_14_ans',
            'F - 15 à 19 ans': 'f_15_19_ans',
            'F - 20 à 24 ans': 'f_20_24_ans',
            'F - 25 à 29 ans': 'f_25_29_ans',
            'F - 30 à 34 ans': 'f_30_34_ans',
            'F - 35 à 39 ans': 'f_35_39_ans',
            'F - 40 à 44 ans': 'f_40_44_ans',
            'F - 45 à 49 ans': 'f_45_49_ans',
            'F - 50 à 54 ans': 'f_50_54_ans',
            'F - 55 à 59 ans': 'f_55_59_ans',
            'F - 60 à 64 ans': 'f_60_64_ans',
            'F - 65 à 69 ans': 'f_65_69_ans',
            'F - 70 à 74 ans': 'f_70_74_ans',
            'F - 75 à 79 ans': 'f_75_79_ans',
            'F - 80 à 99 ans': 'f_80_99_ans',
            'F - NR': 'f_nr',
            'H - 1 à 4 ans': 'h_1_4_ans',
            'H - 5 à 9 ans': 'h_5_9_ans',
            'H - 10 à 14 ans': 'h_10_14_ans',
            'H - 15 à 19 ans': 'h_15_19_ans',
            'H - 20 à 24 ans': 'h_20_24_ans',
            'H - 25 à 29 ans': 'h_25_29_ans',
            'H - 30 à 34 ans': 'h_30_34_ans',
            'H - 35 à 39 ans': 'h_35_39_ans',
            'H - 40 à 44 ans': 'h_40_44_ans',
            'H - 45 à 49 ans': 'h_45_49_ans',
            'H - 50 à 54 ans': 'h_50_54_ans',
            'H - 55 à 59 ans': 'h_55_59_ans',
            'H - 60 à 64 ans': 'h_60_64_ans',
            'H - 65 à 69 ans': 'h_65_69_ans',
            'H - 70 à 74 ans': 'h_70_74_ans',
            'H - 75 à 79 ans': 'h_75_79_ans',
            'H - 80 à 99 ans': 'h_80_99_ans',
            'H - NR': 'h_nr',
            'NR - NR': 'nr_nr',
            'Total': 'total',
        }

        # Supprimer toutes les données de la table Player avant l'insertion
        Player.objects.all().delete()
        print("Anciennes données effacées avant insertion!")

        # Utiliser to_dict avec 'records' pour convertir le DataFrame en une liste de dictionnaires
        players_data = df.rename(columns=column_mapping).to_dict(orient='records')

        # Diviser les données en tranches de 100 000 lignes
        chunk_size = 100000
        for i in range(0, len(players_data), chunk_size):
            chunk = players_data[i:i + chunk_size]
            # Utiliser bulk_create pour insérer les objets Player en une seule requête pour chaque tranche
            Player.objects.bulk_create([Player(**row) for row in chunk])

        print("Script terminé avec succès!")
    except IntegrityError as e:
        print(f"Erreur lors de l'insertion des données : {e}")

if __name__ == "__main__":
    run()
