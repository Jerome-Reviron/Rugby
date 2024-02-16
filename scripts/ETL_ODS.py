import os
import pandas as pd
from datetime import date
from app.models import Club

def run():
    # Charger le fichier CSV dans un DataFrame Pandas
    df = pd.read_csv("data/clubs-data-2021.csv", delimiter=";")

    print(f"Chargement du fichier CSV terminé. Nombre de lignes à insérer : {len(df)}")

    # Tronquer la table Club
    Club.objects.all().delete()
    print("Table Club tronquée.")

    # Extraire l'année à partir du nom du fichier CSV
    year = get_year_from_csv("data/clubs-data-2021.csv")

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
            date=date(year, 1, 1)
        )
        for index, row in df.iterrows()
    ]

    print(f"{len(Clubs)} objets Club créés.")

    # Utiliser bulk_create pour insérer les objets Club en une seule requête
    Club.objects.bulk_create(Clubs)
    print("Insertion des objets Club terminée.")

    # Récupérer les données après bulk_create dans un DataFrame
    df_Club_apres_bulk_create = pd.DataFrame.from_records(Club.objects.values())

def get_year_from_csv(csv_file):
    # Extraire l'année du nom du fichier CSV
    year = None
    file_name, file_ext = os.path.splitext(os.path.basename(csv_file))
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

if __name__ == "__main__":
    run()
