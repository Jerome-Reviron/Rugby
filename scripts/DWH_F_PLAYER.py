import pandas as pd
from app.models import D_CLUB, D_AGEGRP, D_DATE, D_ETABLISHEMENT, D_SEX, F_PLAYER

def run():
    df_club_apres_bulk_create = pd.DataFrame.from_records(D_CLUB.objects.values())
    print(f"Nombre de lignes à insérer dans la table D_CLUB : {len(df_club_apres_bulk_create)}")

    # Créer des instances de D_CLUB à partir du DataFrame
    temp_table_club = []

    for _, row in df_club_apres_bulk_create.iterrows():
        key = f"{row['code']}-{row['code_qpv']}-{row['code_commune']}"
        d_club_instance = D_CLUB(
            code=row['code'],
            code_qpv=row['code_qpv'],
            nom_qpv=row['nom_qpv'],
            federation=row['federation'],
            region=row['region'],
            departement=row['departement'],
            nom_departement=row['nom_departement'],
            code_commune=row['code_commune'],
            commune=row['commune'],
            statut_geo=row['statut_geo'],
            code_code_qpv_code_commune=key,
        )

        # Ajouter la clé primaire dans la table temporaire
        temp_table_club.append({
            'd_club_instance': d_club_instance,
            'd_club_fk': d_club_instance.code_code_qpv_code_commune,
        })

    df_agegrp_apres_bulk_create = pd.DataFrame.from_records(D_AGEGRP.objects.values())
    print(f"Nombre de lignes à insérer dans la table D_AGEGRP : {len(df_agegrp_apres_bulk_create)}")

    # Créer des instances de D_AGEGRP à partir du DataFrame
    temp_table_agegrp = []

    for _, row in df_agegrp_apres_bulk_create.iterrows():
        d_agegrp_instance = D_AGEGRP(
            agegrplabel=row['agegrplabel']
        )

        # Ajouter la clé primaire dans la table temporaire
        temp_table_agegrp.append({
            'd_agegrp_instance': d_agegrp_instance,
            'd_agegrp_fk': d_agegrp_instance.agegrplabel,
        })

    df_date_apres_bulk_create = pd.DataFrame.from_records(D_DATE.objects.values())
    print(f"Nombre de lignes à insérer dans la table D_DATE : {len(df_date_apres_bulk_create)}")

    # Créer des instances de D_DATE à partir du DataFrame
    temp_table_date = []

    for _, row in df_date_apres_bulk_create.iterrows():
        d_date_instance = D_DATE(
            date=row['date']
        )

        # Ajouter la clé primaire dans la table temporaire
        temp_table_date.append({
            'd_date_instance': d_date_instance,
            'd_date_fk': d_date_instance.date,
        })

    df_etablishement_apres_bulk_create = pd.DataFrame.from_records(D_ETABLISHEMENT.objects.values())
    print(f"Nombre de lignes à insérer dans la table D_ETABLISHEMENT : {len(df_etablishement_apres_bulk_create)}")

    # Créer des instances de D_ETABLISHEMENT à partir du DataFrame
    temp_table_etablishement = []

    for _, row in df_etablishement_apres_bulk_create.iterrows():
        d_etablishement_instance = D_ETABLISHEMENT(
            etablishement_id=row['etablishement_id'],
            etablishementlabel=row['etablishementlabel'],
            nombre=row['nombre'],
        )

        # Ajouter la clé primaire dans la table temporaire
        temp_table_etablishement.append({
            'd_etablishement_instance': d_etablishement_instance,
            'd_etablishement_fk': d_etablishement_instance.etablishement_id,
        })

    df_sex_apres_bulk_create = pd.DataFrame.from_records(D_SEX.objects.values())
    print(f"Nombre de lignes à insérer dans la table D_SEX : {len(df_sex_apres_bulk_create)}")


    # Créer des instances de D_SEX à partir du DataFrame
    temp_table_sex = []

    for _, row in df_sex_apres_bulk_create.iterrows():
        d_sex_instance = D_SEX(
            sexcode=row['sexcode']
        )

        # Ajouter la clé primaire dans la table temporaire
        temp_table_sex.append({
            'd_sex_instance': d_sex_instance,
            'd_sex_fk': d_sex_instance.sexcode,
        })        

    # Utiliser bulk_create pour créer les instances de F_PLAYER avec les clés étrangères de D_CLUB, D_AGEGRP, D_DATE et D_ETABLISHEMENT
    f_player_objects = []

    for item_club, item_agegrp, item_date, item_etablishement, item_sex in zip(
        temp_table_club, temp_table_agegrp, temp_table_date, temp_table_etablishement, temp_table_sex
    ):
        # Assurez-vous que chaque relation est sauvegardée individuellement
        d_club_instance = item_club['d_club_instance']
        d_agegrp_instance = item_agegrp['d_agegrp_instance']
        d_date_instance = item_date['d_date_instance']
        d_etablishement_instance = item_etablishement['d_etablishement_instance']
        d_sex_instance = item_sex['d_sex_instance']

        d_club_instance.save()
        d_agegrp_instance.save()
        d_date_instance.save()
        d_etablishement_instance.save()
        d_sex_instance.save()

        # Créez l'objet F_PLAYER avec les relations correctement sauvegardées
        f_player_instance = F_PLAYER(
            D_CLUB_FK=d_club_instance,
            D_AGEGRP_FK=d_agegrp_instance,
            D_DATE_FK=d_date_instance,
            D_ETABLISHEMENT_FK=d_etablishement_instance,
            D_SEX_FK=d_sex_instance,
        )

        f_player_objects.append(f_player_instance)

    F_PLAYER.objects.bulk_create(f_player_objects)

    print("Script terminé avec succès!")

if __name__ == "__main__":
    run()