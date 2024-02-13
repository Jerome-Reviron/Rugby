import os
import pandas as pd
from app.models import Club

def run():
    # Charger le fichier CSV dans un DataFrame Pandas
    df = pd.read_csv("data/clubs-data-2021.csv", delimiter=";")

    print(f"Chargement du fichier CSV terminé. Nombre de lignes à insérer : {len(df)}")

    # Tronquer la table Club
    Club.objects.all().delete()
    print("Table Club tronquée.")

    # Utiliser une compréhension de liste avec to_dict
    Clubs = [
        Club(
            code_commune=row['Code Commune'],
            commune=row['Commune'],
            code_qpv=row['Code QPV'],
            nom_qpv=row['Nom QPV'],
            departement=row['Département'],
            region=row['Région'],
            statut_geo=row['Statut géo'],
            code=row['Code'],
            federation=row['Fédération'],
            clubs=row['Clubs'],
            epa=row['EPA'],
            total=row['Total'],
        )
        for index, row in df.iterrows()
    ]

    print(f"{len(Clubs)} objets Club créés.")

    # Utiliser bulk_create pour insérer les objets Club en une seule requête
    Club.objects.bulk_create(Clubs)
    print("Insertion des objets Club terminée.")

if __name__ == "__main__":
    run()
