import pandas as pd
from django.db import IntegrityError
from app.models import Club, D_ETABLISHEMENT

def run():
    print("Chargement des données de la classe Club...")

    df_Club_apres_bulk_create = pd.DataFrame.from_records(Club.objects.values())
    print("Colonnes de df_Club_apres_bulk_create:", df_Club_apres_bulk_create.columns)
    print(f"Nombre de lignes à insérer dans la table D_ETABLISHEMENT : {len(df_Club_apres_bulk_create)}")

    try:
        # Créer une liste unique de noms de colonnes pour les établissements
        unique_columns = set()
        for column in df_Club_apres_bulk_create.columns:
            # Extraire les établissements (club, epaà partir des noms de colonnes
            etablishement = get_etablishement(column)
            if etablishement:
                unique_columns.add(etablishement)

        # Supprimer toutes les données de la table D_ETABLISHEMENT avant l'insertion
        D_ETABLISHEMENT.objects.all().delete()

        # Utiliser bulk_create pour insérer les objets D_ETABLISHEMENT en une seule requête
        D_ETABLISHEMENT.objects.bulk_create([
            D_ETABLISHEMENT(
                etablishementlabel=etablishement
            )
            for etablishement in unique_columns
        ])

        # Stocker le DataFrame dans une variable
        df_etablishement_apres_bulk_create = pd.DataFrame.from_records(D_ETABLISHEMENT.objects.values())
        print("Colonnes de df_etablishement_apres_bulk_create:", df_etablishement_apres_bulk_create.columns)

        print("Script terminé avec succès!")
    except IntegrityError as e:
        print(f"Erreur lors de l'insertion des données : {e}")

def get_etablishement(column):
    # Logique pour extraire les établissements à partir des noms de colonnes
    if 'clubs' in column.lower():
        return 'clubs'
    elif 'epa' in column.lower():
        return 'epa'
    else:
        return None

if __name__ == "__main__":
    run()
