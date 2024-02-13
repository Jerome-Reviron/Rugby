import pandas as pd
from app.models import D_CLUB, Club

# Tronquer la table D_CLUB
D_CLUB.objects.all().delete()

# Récupérer les données distinctes de la table Club pour les colonnes nécessaires
club_data = Club.objects.values(
    'code', 'nom_qpv', 'federation', 'region', 'departement', 'code_commune', 'commune', 'statut_geo'
).distinct()

# Convertir les données en DataFrames pandas
df_club = pd.DataFrame(club_data)

# Insérer les données dans la table D_CLUB
for _, row in df_club.iterrows():
    D_CLUB.objects.create(
        code=row['code'],
        nom_qpv=row['nom_qpv'],
        federation=row['federation'],
        region=row['region'],
        departement=row['departement'],
        code_commune=row['code_commune'],
        commune=row['commune'],
        statut_geo=row['statut_geo']
    )
