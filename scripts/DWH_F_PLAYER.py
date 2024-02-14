import os
import pandas as pd
from django.db import IntegrityError
from app.models import Player, Club, D_SEX, D_AGEGRP, D_CLUB, D_DATE, D_ETABLISHEMENT, F_PLAYER

def run():
    print("Chargement des données de la classe Player...")
    # Charger les données de la classe Player dans un DataFrame Pandas
    player_data = Player.objects.values('sex_code', 'agegrp_label', 'club', 'date', 'etablissement', 'total')
    df_player = pd.DataFrame.from_records(player_data)

    # Charger les données de la classe Club dans un DataFrame Pandas
    club_data = Club.objects.values('club_name', 'total')
    df_club = pd.DataFrame.from_records(club_data)

    print(f"Nombre de lignes à insérer dans la table F_PLAYER : {len(df_player)}")

    try:
        # Supprimez toutes les données de la table F_PLAYER avant l'insertion
        F_PLAYER.objects.all().delete()
        print("Anciennes données effacées avant insertion!")

        # Utilisez bulk_create pour insérer les objets F_PLAYER en une seule requête
        F_PLAYER.objects.bulk_create([
            F_PLAYER(
                D_SEX_FK=get_or_create_d_sex(row['sex_code']),
                D_AGEGRP_FK=get_or_create_d_agegrp(row['agegrp_label']),
                D_CLUB_FK=get_or_create_d_club(row['club'], df_club),
                D_DATE_FK=get_or_create_d_date(row['date']), 
                D_ETABLISHEMENT_FK=get_or_create_d_etablissement(row['etablissement']), 
                Total_Club=row['total_Club'],
                Total_Player=row['total_Player'],
            )
            for _, row in df_player.iterrows()
        ])

        print("Script terminé avec succès!")
    except IntegrityError as e:
        print(f"Erreur lors de l'insertion des données : {e}")

def get_or_create_d_sex(sex_code):
    obj, created = D_SEX.objects.get_or_create(SexCode=sex_code)
    return obj

def get_or_create_d_agegrp(agegrp_label):
    obj, created = D_AGEGRP.objects.get_or_create(AgeGroupLabel=agegrp_label)
    return obj

def get_or_create_d_club(club, df_club):
    obj, created = D_CLUB.objects.get_or_create(ClubName=club)
    
    # Si le club existe dans le DataFrame, mettez à jour le total
    if created:
        return obj

    club_row = df_club[df_club['club_name'] == club]
    if not club_row.empty:
        obj.Total = club_row.iloc[0]['total']
        obj.save()

    return obj

def get_or_create_d_date(date):
    obj, created = D_DATE.objects.get_or_create(Date=date)
    return obj

def get_or_create_d_etablissement(etablissement):
    obj, created = D_ETABLISHEMENT.objects.get_or_create(EtablissementName=etablissement)
    return obj

if __name__ == "__main__":
    run()
