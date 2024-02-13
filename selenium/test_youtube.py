from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('')
driver.get("http://www.youtube.com")

# Localiser le bouton consentemnt "accept all"
xpath1 = "/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]"
accept_all_element = driver.find_element(By.XPATH, xpath1)
accept_all_element.click()

# Pause pour laisser le temps à la page de se charger complètement après le clic sur le bouton
time.sleep(5)

# Localiser l'input de la barre de recherche
xpath2 = "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input"
search_element = driver.find_element(By.XPATH, xpath2)

# Saisir du texte dans la barre de recherche
search_element.send_keys("Wazoo")

# Appuyer sur la touche "Entrée"
search_element.send_keys(Keys.RETURN)
time.sleep(5)

# Localiser l'élément VIDEO
xpath3 = "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[2]/div[3]/ytd-shelf-renderer[1]/div[1]/div[2]/ytd-vertical-list-renderer/div[1]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/yt-image/img"
time.sleep(5)
start_element = driver.find_element(By.XPATH, xpath3)
start_element.click()

# Localiser l'élément LIKE sous condition d'avoir un compte 'Youtube'
xpath4 = "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/segmented-like-dislike-button-view-model/yt-smartimation/div/div/like-button-view-model/toggle-button-view-model/button-view-model/button/yt-touch-feedback-shape/div/div[2]"
time.sleep(5)
like_element = driver.find_element(By.XPATH, xpath4)
like_element.click()

# Pause avant de fermer le navigateur (ajustez si nécessaire)
time.sleep(100)

driver.close()
