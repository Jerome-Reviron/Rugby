import pandas as pd
# Importez le modèle D_AGEGRP depuis le fichier models.py
from app.models import Player, D_AGEGRP

# Tronquer la table D_AGEGRP
D_AGEGRP.objects.all().delete()

# Liste des colonnes correspondant aux tranches d'âge dans le modèle Player
age_columns = [
    'f_1_4_ans', 'f_5_9_ans', 'f_10_14_ans', 'f_15_19_ans', 'f_20_24_ans',
    'f_25_29_ans', 'f_30_34_ans', 'f_35_39_ans', 'f_40_44_ans', 'f_45_49_ans',
    'f_50_54_ans', 'f_55_59_ans', 'f_60_64_ans', 'f_65_69_ans', 'f_70_74_ans',
    'f_75_79_ans', 'f_80_99_ans', 'f_nr', 'h_1_4_ans', 'h_5_9_ans', 'h_10_14_ans',
    'h_15_19_ans', 'h_20_24_ans', 'h_25_29_ans', 'h_30_34_ans', 'h_35_39_ans',
    'h_40_44_ans', 'h_45_49_ans', 'h_50_54_ans', 'h_55_59_ans', 'h_60_64_ans',
    'h_65_69_ans', 'h_70_74_ans', 'h_75_79_ans', 'h_80_99_ans', 'h_nr', 'nr_nr',
]

# Insérer les données dans la table D_AGEGRP
for column in age_columns:
    # Extraire le libellé de la tranche d'âge à partir du nom de la colonne
    age_label = column.split('_')[1]  # Par exemple, 'f_1_4_ans' devient '1_4_ans'

    # Insérer la tranche d'âge et le libellé correspondant dans la table D_AGEGRP
    D_AGEGRP.objects.create(AgeGrpLabel=age_label)
