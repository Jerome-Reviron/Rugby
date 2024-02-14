import pandas as pd
from django.db import IntegrityError
from app.models import F_PLAYER, D_SEX, D_AGEGRP, D_CLUB, D_DATE, D_ETABLISHEMENT

def run():
    print("Chargement des données de la classe F_PLAYER...")
    # Charger les données de la classe F_PLAYER dans un DataFrame Pandas
    f_player_data = F_PLAYER.objects.values()
    df_f_player = pd.DataFrame.from_records(f_player_data)

    print(f"Nombre de lignes à insérer dans la table F_PLAYER : {len(df_f_player)}")

    try:
        # Supprimer toutes les données de la table F_PLAYER avant l'insertion
        F_PLAYER.objects.all().delete()
        print("Anciennes données effacées avant insertion!")

        # Charger les données des autres classes
        d_sex_data = D_SEX.objects.values()
        df_d_sex = pd.DataFrame.from_records(d_sex_data)

        # Fusionner les DataFrames
        df_f_player = pd.merge(df_f_player, df_d_sex, left_on='SexCode', right_on='SexCode', how='left')

        d_agegrp_data = D_AGEGRP.objects.values()
        df_d_agegrp = pd.DataFrame.from_records(d_agegrp_data)
        df_f_player = pd.merge(df_f_player, df_d_agegrp, left_on='AgeGrpLabel', right_on='AgeGrpLabel', how='left')

        d_club_data = D_CLUB.objects.values()
        df_d_club = pd.DataFrame.from_records(d_club_data)
        df_f_player = pd.merge(df_f_player, df_d_club, left_on='ClubCode', right_on='code_code_qpv_code_commune', how='left')

        d_date_data = D_DATE.objects.values()
        df_d_date = pd.DataFrame.from_records(d_date_data)
        df_f_player = pd.merge(df_f_player, df_d_date, left_on='Date', right_on='Date', how='left')

        d_etablissement_data = D_ETABLISHEMENT.objects.values()
        df_d_etablissement = pd.DataFrame.from_records(d_etablissement_data)
        df_f_player = pd.merge(df_f_player, df_d_etablissement, left_on='EtablishementLabel', right_on='EtablishementLabel', how='left')

        # Supprimer les colonnes inutiles
        df_f_player = df_f_player.drop(['SexCode', 'AgeGrpLabel', 'ClubCode', 'Date', 'EtablishementLabel'], axis=1)

        # Utiliser bulk_create pour insérer les objets F_PLAYER en une seule requête
        F_PLAYER.objects.bulk_create([
            F_PLAYER(
                D_SEX_FK_id=row['SexCode'],
                D_AGEGRP_FK_id=row['AgeGrpLabel'],
                D_CLUB_FK_id=row['ClubCode'],
                D_DATE_FK_id=row['Date'],
                D_ETABLISHEMENT_FK_id=row['EtablishementLabel'],
                Total_Club=row['Total_Club'],
                Total_Player=row['Total_Player']
            )
            for _, row in df_f_player.iterrows()
        ])

        print("Script terminé avec succès!")
    except IntegrityError as e:
        print(f"Erreur lors de l'insertion des données : {e}")

if __name__ == "__main__":
    run()
