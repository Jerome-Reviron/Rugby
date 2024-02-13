import pandas as pd
from app.models import Club, D_COMMUNE

# Tronquer la table D_COMMUNE
D_COMMUNE.objects.all().delete()

# Récupérer les données distinctes de la table Club pour les colonnes code_commune et commune
commune_data = Club.objects.values('code_commune', 'commune').distinct()

# Convertir les données en DataFrame pandas
df_commune = pd.DataFrame(commune_data)

# Insérer les données dans la table D_COMMUNE
for _, row in df_commune.iterrows():
    D_COMMUNE.objects.create(code_commune=row['code_commune'], commune=row['commune'])