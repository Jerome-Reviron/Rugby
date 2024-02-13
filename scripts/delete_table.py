from django.db import connections

def delete_geopostion_table():
    # Nom de la table à supprimer
    table_name = 'app_d_geopostion'

    # Récupérer la connexion par défaut
    connection = connections['default']

    # Créer un curseur
    with connection.cursor() as cursor:
        # Exécuter la requête SQL de suppression de table
        cursor.execute(f'DROP TABLE IF EXISTS {table_name}')

    print(f"La table '{table_name}' a été supprimée avec succès.")

# Appeler la fonction pour supprimer la table
delete_geopostion_table()