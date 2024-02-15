import pandas as pd
from django.db import IntegrityError
from app.models import F_PLAYER, D_SEX, D_AGEGRP, D_CLUB, D_DATE, D_ETABLISHEMENT, Player, Club

def run():
    print("Chargement des données...")
    # Charger les données des classes dimensionnelles dans des DataFrames Pandas
    player_data = Player.objects.values()
    df_player = pd.DataFrame.from_records(player_data)
    print("Colonnes dans le DataFrame 'Player' : ", df_player.columns)

    club_data = Club.objects.values()
    df_club = pd.DataFrame.from_records(club_data)
    print("Colonnes dans le DataFrame 'Club' : ", df_club.columns)

    d_sex_data = D_SEX.objects.values()
    df_d_sex = pd.DataFrame.from_records(d_sex_data)
    print("Colonnes dans le DataFrame 'D_SEX' : ", df_d_sex.columns)

    d_agegrp_data = D_AGEGRP.objects.values()
    df_d_agegrp = pd.DataFrame.from_records(d_agegrp_data)
    print("Colonnes dans le DataFrame 'D_AGEGRP' : ", df_d_agegrp.columns)

    d_club_data = D_CLUB.objects.values()
    df_d_club = pd.DataFrame.from_records(d_club_data)
    print("Colonnes dans le DataFrame 'D_CLUB' : ", df_d_club.columns)

    d_date_data = D_DATE.objects.values()
    df_d_date = pd.DataFrame.from_records(d_date_data)
    print("Colonnes dans le DataFrame 'D_DATE' : ", df_d_date.columns)

    d_etablissement_data = D_ETABLISHEMENT.objects.values()
    df_d_etablissement = pd.DataFrame.from_records(d_etablissement_data)
    print("Colonnes dans le DataFrame 'D_ETABLISHEMENT' : ", df_d_etablissement.columns)

    df_f_player = pd.DataFrame()

    # Remplir df_f_player en joignant les DataFrames dimensionnels
    # (remplacer 'key' par la clé appropriée pour chaque fusion)
    df_f_player = pd.merge(df_player, df_d_sex, on='sexcode', how='inner')
    df_f_player = pd.merge(df_f_player, df_d_agegrp, on='agegrplabel', how='inner')
    df_f_player = pd.merge(df_f_player, df_d_club, on='code_code_qpv_code_commune', how='inner')
    df_f_player = pd.merge(df_f_player, df_d_date, on='date', how='inner')
    df_f_player = pd.merge(df_f_player, df_d_etablissement, on='etablishement_id', how='inner')

    print(f"Nombre de lignes à insérer dans la table F_PLAYER : {len(df_f_player)}")

    try:
        # Supprimer toutes les données de la table F_PLAYER avant l'insertion
        F_PLAYER.objects.all().delete()
        print("Anciennes données effacées avant insertion!")

        # Utiliser bulk_create pour insérer les objets F_PLAYER en une seule requête
        F_PLAYER.objects.bulk_create([
            F_PLAYER(
                D_SEX_FK_id=row['sexcode'],
                D_AGEGRP_FK_id=row['agegrplabel'],
                D_CLUB_FK_id=row['code_code_qpv_code_commune'],
                D_DATE_FK_id=row['date'],
                D_ETABLISHEMENT_FK_id=row['etablishement_id'],
                Total_Club=row['Total_Club'],
                Total_Player=row['Total_Player'],
                date_table=row['date_table']
            )
            for _, row in df_f_player.iterrows()
        ])

        print("Script terminé avec succès!")
    except IntegrityError as e:
        print(f"Erreur lors de l'insertion des données : {e}")

if __name__ == "__main__":
    run()
