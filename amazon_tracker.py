from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



# Dans un premier temps je vais mettre en place une classe qui me permettra de recueillir la data voulu
class AmazonData:
  def __init__(self, search_term, base_url, currency):
    self.search_term = search_term
    self.base_url = base_url
    options = self.get_chrome_options()
    self.driver = self.get_chrome_web_driver(options)
    self.currency = currency
    
    
    # Methode qui permet d'ouvrir le navigateur Chrome
  def get_chrome_web_driver(self, options):
    service = ChromeService('./chromedriver')
    return webdriver.Chrome(service=service, options=options)

  def get_chrome_options(self):
    return webdriver.ChromeOptions()

  def run_script(self):
    print("Lancement du script")
    print(f"Recherche de produits {self.search_term}")
    links = self.get_products_links()
    time.sleep(5)
    self.driver.quit()
    # if not links:
    #   print("Stopped script.")
    #   return

  def get_products_links(self):
    self.driver.get(self.base_url)
    element = self.driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')
    element.send_keys(self.search_term)
    element.send_keys(Keys.ENTER)
    time.sleep(5)
    self.driver.get(f'{self.driver.current_url}')
    
    

  def get_products_info(self):
    pass
  
  def get_asins(self):
    pass
  
  def get_product_single_info(self):
    pass

  def get_title(self):
    pass

  def get_price(self):
    pass

  def get_seller(self):
    pass

  def get_rating(self):
    pass

