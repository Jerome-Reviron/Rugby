import random

# Associez chaque numéro à un nom
noms = {1: "johlan", 2: "coulibaly", 3: "jérôme", 4: "léo", 5: "raphael", 6: "pierre"}

# Inversez le dictionnaire pour obtenir une correspondance de nom à numéro
noms_inverse = {v: k for k, v in noms.items()}

# Utilisation de la fonction random.choice pour choisir un nom au hasard parmi la liste des noms
nom_tire = random.choice(list(noms.values()))

# Affichage du nom tiré au sort et son numéro associé
print("Le nom tiré au sort est :", nom_tire)
print("Le numéro associé est :", noms_inverse[nom_tire])
