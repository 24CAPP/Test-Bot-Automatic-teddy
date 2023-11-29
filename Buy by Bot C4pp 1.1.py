from selenium import webdriver
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import json

options = webdriver.FirefoxOptions()
options.headless = False

driver = webdriver.Firefox(options=options)

driver.get('https://www.teddyallmarket.it/my-account-2/')

# Trova il pulsante "Accedi" utilizzando il selettore CSS
accedi_button = driver.find_element(By.CSS_SELECTOR, 'button.woocommerce-button.button.woocommerce-form-login__submit')

# Carica le credenziali dal file JSON
with open('credenziali.json', 'r') as file:
    credentials = json.load(file)

username = credentials['username']
password = credentials['password']

username_field = driver.find_element(By.ID, 'username')
password_field = driver.find_element(By.ID, 'password')

username_field.send_keys(username)
password_field.send_keys(password)

# Fai click sul pulsante "Accedi" dopo aver inserito le credenziali
accedi_button.click()

# Aspetta un po' per assicurarti che la pagina si carichi completamente dopo il login
time.sleep(5)

# Naviga direttamente al link specificato
driver.get('https://www.teddyallmarket.it/product/air-jordan-1-retro-high-j-balvin/')


# Attendi che la pagina si carichi completamente dopo essere navigati al prodotto desiderato
time.sleep(5)  # Puoi regolare questo valore se necessario

# Individua l'elemento select
numero_select = driver.find_element(By.ID, 'numero')

# Seleziona l'opzione corrispondente al numero 42 utilizzando la classe Select di Selenium
select = Select(numero_select)
select.select_by_value('42')

# Attendi che la pagina si carichi completamente dopo essere navigati al prodotto desiderato
time.sleep(2)  # Puoi regolare questo valore se necessario

# Numero di clic che si desidera effettuare (10 volte)
num_clicks = 10

for _ in range(num_clicks):
    # Individua il pulsante "Aggiungi al carrello" ogni volta prima di fare clic su di esso
    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, 'button.single_add_to_cart_button')
    add_to_cart_button.click()
    time.sleep(1)  # Ritardo di 3 secondi tra i clic


# Naviga alla pagina di checkout
driver.get('https://www.teddyallmarket.it/checkout-2/')
