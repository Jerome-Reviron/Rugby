import pandas as pd
from django.db import IntegrityError
from app.models import Player

def run():
    print("Chargement du fichier CSV...")
    # Charger le fichier CSV dans un DataFrame Pandas
    df = pd.read_csv("data/lic-data-2021.csv", delimiter=";", dtype=str)

    print(f"Nombre de lignes à insérer : {len(df)}")

    try:
        # Ajouter une condition pour exclure les lignes où 'Code Commune' est égal à "NR - Non réparti"
        players_data = [
            Player(
                code_commune=row['Code Commune'],
                commune=row['Commune'],
                code_qpv=row['Code QPV'],
                nom_qpv=row['Nom QPV'],
                departement=row['Département'],
                region=row['Région'],
                statut_geo=row['Statut géo'],
                code=row['Code'],
                federation=row['Fédération'],
                f_1_4_ans=row['F - 1 à 4 ans'],
                f_5_9_ans=row['F - 5 à 9 ans'],
                f_10_14_ans=row['F - 10 à 14 ans'],
                f_15_19_ans=row['F - 15 à 19 ans'],
                f_20_24_ans=row['F - 20 à 24 ans'],
                f_25_29_ans=row['F - 25 à 29 ans'],
                f_30_34_ans=row['F - 30 à 34 ans'],
                f_35_39_ans=row['F - 35 à 39 ans'],
                f_40_44_ans=row['F - 40 à 44 ans'],
                f_45_49_ans=row['F - 45 à 49 ans'],
                f_50_54_ans=row['F - 50 à 54 ans'],
                f_55_59_ans=row['F - 55 à 59 ans'],
                f_60_64_ans=row['F - 60 à 64 ans'],
                f_65_69_ans=row['F - 65 à 69 ans'],
                f_70_74_ans=row['F - 70 à 74 ans'],
                f_75_79_ans=row['F - 75 à 79 ans'],
                f_80_99_ans=row['F - 80 à 99 ans'],
                f_nr=row['F - NR'],
                h_1_4_ans=row['H - 1 à 4 ans'],
                h_5_9_ans=row['H - 5 à 9 ans'],
                h_10_14_ans=row['H - 10 à 14 ans'],
                h_15_19_ans=row['H - 15 à 19 ans'],
                h_20_24_ans=row['H - 20 à 24 ans'],
                h_25_29_ans=row['H - 25 à 29 ans'],
                h_30_34_ans=row['H - 30 à 34 ans'],
                h_35_39_ans=row['H - 35 à 39 ans'],
                h_40_44_ans=row['H - 40 à 44 ans'],
                h_45_49_ans=row['H - 45 à 49 ans'],
                h_50_54_ans=row['H - 50 à 54 ans'],
                h_55_59_ans=row['H - 55 à 59 ans'],
                h_60_64_ans=row['H - 60 à 64 ans'],
                h_65_69_ans=row['H - 65 à 69 ans'],
                h_70_74_ans=row['H - 70 à 74 ans'],
                h_75_79_ans=row['H - 75 à 79 ans'],
                h_80_99_ans=row['H - 80 à 99 ans'],
                h_nr=row['H - NR'],
                nr_nr=row['NR - NR'],
                total=row['Total'],
            )
            for index, row in df.iterrows()
        ]

        # Supprimer toutes les données de la table Player avant l'insertion
        Player.objects.all().delete()
        print("Anciennes données effacées avant insertion!")

        # Utiliser bulk_create pour insérer les objets Player en une seule requête
        Player.objects.bulk_create(players_data)
        
        # Récupérer les données après bulk_create dans un DataFrame
        df_Player_apres_bulk_create = pd.DataFrame.from_records(Player.objects.values())

        print("Script terminé avec succès!")
    except IntegrityError as e:
        print(f"Erreur lors de l'insertion des données : {e}")

if __name__ == "__main__":
    run()
