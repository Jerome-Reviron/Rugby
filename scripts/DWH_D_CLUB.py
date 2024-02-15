import pandas as pd
from django.db import IntegrityError
from app.models import Club, D_CLUB

def run():
    print("Chargement des données de la classe Club...")
    # Charger les données de la classe Club dans un DataFrame Pandas
    club_data = Club.objects.exclude(code_commune="NR - Non réparti").values()
    df_club = pd.DataFrame.from_records(club_data)

    print(f"Nombre de lignes à insérer dans la table D_CLUB : {len(df_club)}")

    try:
        # Supprimer toutes les données de la table D_CLUB avant l'insertion
        D_CLUB.objects.all().delete()
        print("Anciennes données effacées avant insertion!")

        # Utiliser bulk_create pour insérer les objets D_CLUB en une seule requête
        d_club_objects = []
        for _, row in df_club.iterrows():
            key = f"{row['code']}-{row['code_qpv']}-{row['code_commune']}"
            d_club_objects.append(D_CLUB(
                code=row['code'],
                code_qpv=row['code_qpv'],
                nom_qpv=row['nom_qpv'],
                federation=row['federation'],
                region=row['region'],
                departement=row['departement'],
                nom_departement=row.get('nom_departement', ''),
                code_commune=row['code_commune'],
                commune=row['commune'],
                statut_geo=row['statut_geo'],
                code_code_qpv_code_commune=key,
            ))

        D_CLUB.objects.bulk_create(d_club_objects)

        print("Script terminé avec succès!")
    except IntegrityError as e:
        print(f"Erreur lors de l'insertion des données : {e}")

if __name__ == "__main__":
    run()