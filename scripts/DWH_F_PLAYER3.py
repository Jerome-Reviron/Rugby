import pandas as pd
from app.models import D_CLUB, D_SEX, D_AGEGRP, D_DATE, D_ETABLISHEMENT, F_PLAYER
from django.db import transaction

def run():

    df_fact = pd.read_csv('data/df_fact.csv', sep=';')
    df_fact = df_fact.query('region == "Auvergne-Rhône-Alpes" and code_commune != "NR - Non réparti" and nombre_club != 0 and nombre_player != 0')

    # Liste pour stocker les objets F_PLAYER
    f_player_objects = []
    total_rows = len(f_player_objects)

    # Supprimer toutes les entrées existantes dans la table F_PLAYER
    F_PLAYER.objects.all().delete()

    # Utiliser une transaction atomique pour garantir l'intégrité de la base de données
    with transaction.atomic():
        total_rows_inserted = 0
        try:
            # Itérer sur les lignes de df_fact
            for _, row in df_fact.iterrows():
                # Créer des instances de D_CLUB, D_AGEGRP, D_DATE, D_ETABLISHEMENT, D_SEX
                d_club_instance = D_CLUB(
                    code_code_qpv_code_commune=row['code_code_qpv_code_commune'],
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
                d_sex_instance = D_SEX(
                    sexcode=row['sexcode']
                )
                d_agegrp_instance = D_AGEGRP(
                    agegrplabel=row['agegrplabel']
                )
                d_date_instance = D_DATE(
                    date=row['date']
                )
                d_etablishement_instance = D_ETABLISHEMENT(
                    etablishementlabel=row['etablishementlabel']
                )

                # Enregistrez les instances de D_CLUB, D_AGEGRP, D_DATE, D_ETABLISHEMENT, D_SEX
                d_club_instance.save()
                d_sex_instance.save()
                d_agegrp_instance.save()
                d_date_instance.save()
                d_etablishement_instance.save()

                # Créer la clé primaire concaténée
                D_5_PK = f"{row['code_code_qpv_code_commune']}_{row['date']}_{row['etablishementlabel']}_{row['sexcode']}_{row['agegrplabel']}"

                # Créer l'objet F_PLAYER avec les relations correctement sauvegardées
                f_player_instance = F_PLAYER(
                    D_5_PK,
                    D_CLUB_FK=d_club_instance,
                    D_SEX_FK=d_sex_instance,
                    D_AGEGRP_FK=d_agegrp_instance,
                    D_DATE_FK=d_date_instance,
                    D_ETABLISHEMENT_FK=d_etablishement_instance,
                    nombre_club=row['nombre_club'],
                    nombre_player=row['nombre_player']
                )

                f_player_objects.append(f_player_instance)

                # Mettre à jour le nombre total de lignes insérées
                total_rows_inserted += 1

                # Afficher un message à chaque itération
                if total_rows_inserted % 1000 == 0:
                    print(f"{total_rows_inserted} lignes insérées...")

            # Afficher le nombre total de lignes qui seront insérées
            print(f"Nombre total de lignes à insérer : {total_rows_inserted}")

            # Utilisation de bulk_create avec ignore_conflicts=True
            F_PLAYER.objects.bulk_create(f_player_objects, ignore_conflicts=True)

            print(f"Script terminé avec succès! {total_rows_inserted} lignes insérées.")
        except Exception as e:
            print(f"Une erreur s'est produite pendant l'insertion : {str(e)}")

if __name__ == "__main__":
    run()
