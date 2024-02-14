import pandas as pd
from django.db import IntegrityError
from app.models import Player, D_AGEGRP

def run():
    print("Chargement des données de la classe Player...")
    # Charger les données de la classe Player dans un DataFrame Pandas
    player_data = Player.objects.values()
    df_player = pd.DataFrame.from_records(player_data)

    print(f"Nombre de lignes à insérer dans la table D_AGEGRP : {len(df_player)}")

    try:
        # Créer une liste unique de noms de colonnes
        unique_columns = set()
        for column in df_player.columns:
            # Extraire le label d'âge à partir des noms de colonnes
            agegrp_label = get_agegrp_label(column)
            if agegrp_label:
                unique_columns.add(agegrp_label)

        # Supprimer toutes les données de la table D_AGEGRP avant l'insertion
        D_AGEGRP.objects.all().delete()
        print("Anciennes données effacées avant insertion!")

        # Utiliser bulk_create pour insérer les objets D_AGEGRP en une seule requête
        D_AGEGRP.objects.bulk_create([
            D_AGEGRP(
                AgeGrpLabel=agegrp_label
            )
            for agegrp_label in unique_columns
        ])

        print("Script terminé avec succès!")
    except IntegrityError as e:
        print(f"Erreur lors de l'insertion des données : {e}")

def get_agegrp_label(column):
    # Logique pour extraire la partie après le premier '_' et avant 'ans' dans le nom de la colonne
    parts = column.split('_')
    if len(parts) > 1 and parts[-1] == 'ans':
        return f"_{parts[1]}_{parts[2]}_{parts[3]}_ans"
    else:
        return None

if __name__ == "__main__":
    run()
