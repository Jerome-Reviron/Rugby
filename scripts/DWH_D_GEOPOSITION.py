import pandas as pd
from app.models import Club, D_GEOPOSITION

D_GEOPOSITION.objects.all().delete()

# Récupérer les données distinctes de la table Club pour les colonnes region, departement et statut_geo
geoposition_data = Club.objects.values('region', 'departement', 'statut_geo').distinct()

# Convertir les données en DataFrame pandas
df_geoposition = pd.DataFrame(geoposition_data)

# Insérer les données dans la table D_GEOPOSTION
for _, row in df_geoposition.iterrows():
    D_GEOPOSITION.objects.create(region=row['region'], departement=row['departement'], statut_geo=row['statut_geo'])