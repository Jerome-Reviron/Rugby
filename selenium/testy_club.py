from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime

driver = webdriver.Chrome('')
driver.get("http://localhost:8000/")

# Recherchez l'élément sur la page en utilisant le chemin XPath
element = driver.find_element(By.XPATH, "/html/body/div/div[1]/p")

time.sleep(5)

# Obtenez le texte de l'élément
element_text = element.text

# Obtenir la date et l'heure actuelles
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Ouvrir le fichier "logs" en mode append et enregistrer avec la date
with open("selenium/logs", "a") as f:
    f.write(f"{current_datetime} - {element_text}\n")

# Fermez le navigateur
driver.close()
