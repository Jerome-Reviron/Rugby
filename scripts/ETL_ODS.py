import os
import pandas as pd
from datetime import datetime
from app.models import Club

def run():
    # Charger le fichier CSV dans un DataFrame Pandas
    df = pd.read_csv("data/clubs-data-2021.csv", delimiter=";")

    # Tronquer la table Club
    Club.objects.all().delete()

    Clubs = []
    # Parcourir les lignes du DataFrame et insérer dans la table Club
    for index, row in df.iterrows():
        # Ajouter d'autres champs selon vos besoins
        obj = Club(
            code_commune = row['Code Commune'],
            commune = row['Commune'],
            code_qpv = row['Code QPV'],
            nom_qpv = row['Nom QPV'],
            departement = row['Département'],
            region = row['Région'],
            statut_geo = row['Statut géo'],
            code = row['Code'],
            federation = row['Fédération'],
            clubs = row['Clubs'],
            epa = row['EPA'],
            total = row['Total'],
            creation_date = datetime.now()
        )
        Clubs.append(obj)

    Club.objects.bulk_create(Clubs)

if __name__ == "__main__":
    run()
