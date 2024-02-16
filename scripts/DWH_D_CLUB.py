from django.db import IntegrityError
import pandas as pd
from app.models import D_CLUB, Club

def run():
    print("Chargement des données de la classe Club...")

    df_Club_apres_bulk_create = pd.DataFrame.from_records(Club.objects.values())
    df_club = df_Club_apres_bulk_create[(df_Club_apres_bulk_create['region'] == "Auvergne-Rhône-Alpes") 
                                    & (df_Club_apres_bulk_create['code_commune'] != "NR - Non réparti")]

    # Tri du DataFrame selon les colonnes spécifiées
    df_club_sorted = df_club.sort_values(by=['code', 'code_qpv', 'code_commune'])
    print("Colonnes de df_club:", df_club.columns)

    print(f"Nombre de lignes à insérer dans la table D_CLUB : {len(df_club)}")

    try:
        # Supprimer toutes les données de la table D_CLUB avant l'insertion
        D_CLUB.objects.all().delete()
        print("Anciennes données effacées avant insertion!")

        for _, row in df_club_sorted.iterrows():
            key = f"{row['code']}-{row['code_qpv']}-{row['code_commune']}"
            D_CLUB.objects.update_or_create(
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

        # Stocker le DataFrame dans une variable
        df_club_apres_bulk_create = pd.DataFrame.from_records(D_CLUB.objects.values())

        print("Script terminé avec succès!")
    except IntegrityError as e:
        print(f"Erreur lors de l'insertion des données : {e}")

if __name__ == "__main__":
    run()
