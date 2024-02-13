import pandas as pd
from app.models import Club, D_QPV

# Tronquer la table D_QPV
D_QPV.objects.all().delete()

# Récupérer les données distinctes de la table Club pour les colonnes code_qpv et nom_qpv
qpv_data = Club.objects.values('code_qpv', 'nom_qpv').distinct()

# Convertir les données en DataFrames pandas
df_qpv = pd.DataFrame(qpv_data)

# Insérer les données dans la table D_QPV
for _, row in df_qpv.iterrows():
    D_QPV.objects.create(code_qpv=row['code_qpv'], nom_qpv=row['nom_qpv'])
