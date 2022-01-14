from selenium import webdriver
from selenium.webdriver.chrome.service import Service

DIRECTORY = 'reports'
NAME = 'PS4'
CURRENCY = '€'
MIN_PRICE = '275'
MAX_PRICE = '650'
FILTERS = {
    'min': MIN_PRICE,
    'max': MAX_PRICE
}
BASE_URL = "https://www.amazon.fr/"


service = Service("chromedriver")

# Methode qui permet d'ouvrir le navigateur Chrome
def get_chrome_web_driver(options):
  return webdriver.Chrome(service, chrome_options=options)

def get_chrome_options():
  return webdriver.ChromeOptions()

