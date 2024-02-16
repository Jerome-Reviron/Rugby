import pandas as pd
from django.db import IntegrityError
from app.models import Player, D_SEX

def run():
    print("Chargement des données de la classe Player...")
    # Charger les données de la classe Player dans un DataFrame Pandas
    df_Player_apres_bulk_create = pd.DataFrame.from_records(Player.objects.values())
    df_player = pd.DataFrame.from_records(df_Player_apres_bulk_create)
    print(f"Nombre de lignes à insérer dans la table D_SEX : {len(df_player)}")

    try:
        # Créer une liste unique de noms de colonnes
        unique_columns = set()
        for column in df_player.columns:
            # Extraire le code de sexe (F, H, NR) à partir des noms de colonnes
            sex_code = get_sex_code(column)
            if sex_code and sex_code != 'nr':
                unique_columns.add(sex_code)

        # Supprimer toutes les données de la table D_SEX avec le code 'nr' avant l'insertion
        D_SEX.objects.filter(sexcode='nr').delete()

        # Utiliser bulk_create pour insérer les objets D_SEX en une seule requête
        D_SEX.objects.bulk_create([
            D_SEX(
                sexcode=sex_code
            )
            for sex_code in unique_columns
        ])

        # Stocker le DataFrame dans une variable
        df_sex_apres_bulk_create = pd.DataFrame.from_records(D_SEX.objects.values())

        print("Script terminé avec succès!")
    except IntegrityError as e:
        print(f"Erreur lors de l'insertion des données : {e}")

def get_sex_code(column):
    # Logique pour extraire le code de sexe à partir des noms de colonnes
    if 'f' in column.lower():
        return 'f'
    elif 'h' in column.lower():
        return 'h'
    elif 'nr' in column.lower():
        return 'nr'
    else:
        return None

if __name__ == "__main__":
    run()
