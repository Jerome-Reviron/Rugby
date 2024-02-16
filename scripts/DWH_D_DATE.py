import os
import pandas as pd
from datetime import date
from django.db import IntegrityError
from app.models import Player, D_DATE

def run():
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


            print("Script terminé avec succès!")
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
    
if __name__ == "__main__":
    run()
