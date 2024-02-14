import pandas as pd
from django.db import IntegrityError
from app.models import Club, D_ETABLISHEMENT

def run():
    print("Chargement des données de la classe Club...")
    # Charger les données de la classe Club dans un DataFrame Pandas
    club_data = Club.objects.values()
    df_club = pd.DataFrame.from_records(club_data)

    print(f"Nombre de lignes à insérer dans la table D_ETABLISHEMENT : {len(df_club)}")

    try:
        # Supprimer toutes les données de la table D_ETABLISHEMENT avant l'insertion
        D_ETABLISHEMENT.objects.all().delete()
        print("Anciennes données effacées avant insertion!")

        # Utiliser bulk_create pour insérer les objets D_ETABLISHEMENT en une seule requête
        D_ETABLISHEMENT.objects.bulk_create([
            D_ETABLISHEMENT(
                EtablishementLabel=get_etablishment_label(row),
                Nombre=get_nombre_value(row),
            )
            for index, row in df_club.iterrows()
        ])

        print("Script terminé avec succès!")
    except IntegrityError as e:
        print(f"Erreur lors de l'insertion des données : {e}")

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

if __name__ == "__main__":
    run()
