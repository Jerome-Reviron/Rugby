from django.db import IntegrityError
import pandas as pd
from app.models import D_CLUB, Club

def run():
    print("Chargement des données de la classe Club...")
    
    # Charger les données de la classe Club dans un DataFrame Pandas
    club_data = Club.objects.filter(region="Auvergne-Rhône-Alpes").values()
    df_club = pd.DataFrame.from_records(club_data)
    print("Colonnes de df_club:", df_club.columns)

    print(f"Nombre de lignes à insérer dans la table D_CLUB : {len(df_club)}")

    try:
        # Supprimer toutes les données de la table D_CLUB avant l'insertion
        D_CLUB.objects.all().delete()
        print("Anciennes données effacées avant insertion!")

        # Utiliser bulk_create pour insérer les objets D_CLUB en une seule requête
        d_club_objects = []

        for _, row in df_club.iterrows():
            if row['code_commune'] != "NR - Non réparti":
                key = f"{row['code']}-{row['code_qpv']}-{row['code_commune']}"
                
                try:
                    # Essayez de mettre à jour l'enregistrement s'il existe, sinon créez-le
                    obj, created = D_CLUB.objects.update_or_create(
                        code_code_qpv_code_commune=key,
                        defaults={
                            'code': row['code'],
                            'code_qpv': row['code_qpv'],
                            'nom_qpv': row['nom_qpv'],
                            'federation': row['federation'],
                            'region': row['region'],
                            'departement': row['departement'],
                            'code_commune': row['code_commune'],
                            'commune': row['commune'],
                            'statut_geo': row['statut_geo'],
                        }
                    )
                    
                    if not created:
                        print(f"Enregistrement existant : {key}")
                except IntegrityError as e:
                    print(f"Ignoré (déjà existant) : {key}")

        # Stocker le DataFrame dans une variable
        df_club_apres_bulk_create = pd.DataFrame.from_records(D_CLUB.objects.values())

        print("Script terminé avec succès!")
    except IntegrityError as e:
        print(f"Erreur lors de l'insertion des données : {e}")

if __name__ == "__main__":
    run()
