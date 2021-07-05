#importação
from selenium.webdriver.common.keys import Keys
from selenium import webdriver #importe do selenium webdriver "controlador" de site
from selenium.webdriver.firefox.options import Options #import do controlador especifico do firefox
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import time #biblioteca para adicionar um tempo de espera 
from bs4 import BeautifulSoup #manipular html

class marionette():
    options = Options()# instancinado 
    options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"#adicionando o caminho do navagado ao codigo
    driver = webdriver.Firefox(options=options, executable_path="C:/Users/dougl/Desktop/Nova pasta/geckodriver-v0.29.1-win64/2/geckodriver.exe")#adiconando o caminho do controlador de navegador

    def on_marionette(link,driver):
         elemento=driver.get(link)
         time.sleep(20)
         print('aguarde pedido de autentificação')

driver=marionette.driver
link='https://web.whatsapp.com/'
marionette.on_marionette(link,driver)