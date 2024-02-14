import pandas as pd
from django.db import IntegrityError
from app.models import F_PLAYER, D_SEX, D_AGEGRP, D_CLUB, D_DATE, D_ETABLISHEMENT, Club, Player

def run():
    print("Chargement des données de la classe F_PLAYER...")

    # Charger les données de la classe F_PLAYER dans un DataFrame Pandas
    # Assurez-vous d'avoir les colonnes nécessaires dans le DataFrame
    f_player_data = pd.merge(
        Club.objects.values(),
        Player.objects.values(),
        how='inner',
        on=['code_qpv', 'code', 'federation']
    )

    print(f"Nombre de lignes à insérer dans la table F_PLAYER : {len(f_player_data)}")

    try:
        # Supprimer toutes les données de la table F_PLAYER avant l'insertion
        F_PLAYER.objects.all().delete()
        print("Anciennes données effacées avant insertion!")

        # Utiliser bulk_create pour insérer les objets F_PLAYER en une seule requête
        f_player_objects = []
        for _, row in f_player_data.iterrows():
            # Récupérer les clés étrangères correspondantes
            d_sex_fk = D_SEX.objects.get(your_condition=row['SexCode'])
            d_agegrp_fk = D_AGEGRP.objects.get(your_condition=row['AgeGrpLabel'])
            d_club_fk = D_CLUB.objects.get(your_condition=row['code_code_qpv_code_commune'])
            d_date_fk = D_DATE.objects.get(your_condition=row['Date'])
            d_etablissement_fk = D_ETABLISHEMENT.objects.get(your_condition=row['your_condition'])

            # Créer l'objet F_PLAYER
            f_player_objects.append(F_PLAYER(
                D_SEX_FK=d_sex_fk,
                D_AGEGRP_FK=d_agegrp_fk,
                D_CLUB_FK=d_club_fk,
                D_DATE_FK=d_date_fk,
                D_ETABLISHEMENT_FK=d_etablissement_fk,
                Total_Club=row['total'],
                Total_Player=row['total'],
            ))

        F_PLAYER.objects.bulk_create(f_player_objects)

        print("Script terminé avec succès!")
    except IntegrityError as e:
        print(f"Erreur lors de l'insertion des données : {e}")

if __name__ == "__main__":
    run()