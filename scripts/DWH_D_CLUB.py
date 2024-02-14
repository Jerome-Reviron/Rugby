import pandas as pd
from django.db import IntegrityError
from app.models import Club, D_CLUB

def run():
    print("Chargement des données de la classe Club...")
    # Charger les données de la classe Club dans un DataFrame Pandas
    club_data = Club.objects.values()
    df_club = pd.DataFrame.from_records(club_data)

    print(f"Nombre de lignes à insérer dans la table D_CLUB : {len(df_club)}")

    try:
        # Supprimer toutes les données de la table D_CLUB avant l'insertion
        D_CLUB.objects.all().delete()
        print("Anciennes données effacées avant insertion!")

        # Utiliser bulk_create pour insérer les objets D_CLUB en une seule requête
        D_CLUB.objects.bulk_create([
            D_CLUB(
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
            for index, row in df_club.iterrows()
        ])

        print("Script terminé avec succès!")
    except IntegrityError as e:
        print(f"Erreur lors de l'insertion des données : {e}")

if __name__ == "__main__":
    run()
