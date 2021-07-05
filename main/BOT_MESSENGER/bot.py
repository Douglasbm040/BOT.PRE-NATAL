#importação
from selenium.webdriver.common.keys import Keys
from selenium import webdriver #importe do selenium webdriver "controlador" de site
from selenium.webdriver.firefox.options import Options #import do controlador especifico do firefox
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import time #biblioteca para adicionar um tempo de espera 
from bs4 import BeautifulSoup #manipular html



class Bot_messenger:
    link='https://web.whatsapp.com/'
    contact="É eu msm"

 

    def on_marionette(link):
        options = Options()# instancinado 
        options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"#adicionando o caminho do navagado ao codigo
        driver = webdriver.Firefox(options=options, executable_path="C:/Users/dougl/Desktop/Nova pasta/geckodriver-v0.29.1-win64/2/geckodriver.exe")#adiconando o caminho do controlador de navegador
        elemento=driver.get(link)
        time.sleep(20)
        print('aguarde pedido de autentificação')
        return driver
     
    driver= on_marionette(link)
    

    def authentication(driver):
        print('por favor autentifique-se')
        while True:
            try :
                elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[3]/div/header/div[2]/div/span/div[2]/div/span')
                authentication=True

            except:
                authentication=False
                

            if authentication==True:
                print('autentificado !')
                break
        return authentication 
    

    def clear_box_contact(driver):
        print('buscando caixa de busca de contato')
        elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[3]/div/header/div[2]/div/span/div[2]/div/span').click()
        time.sleep(20)
        print('limpando caixa de busca de contato')
        elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[1]/div/label/div/div[2]').clear()
        print('caixa de busca de contato limpa') 

    def search_contact(contact,driver):
        print('digitando nome do contato')
        time.sleep(20)
        elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[1]/div/label/div/div[2]').send_keys(contact)

    def acess_contact(driver):
        print('acessando contato ')
        time.sleep(10)
        elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/span').click()

    def write(mensagem,driver):
        print('limpando caixa de texto')
        elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]').clear() 
        print('escrevendo para o contato')
        time.sleep(20)
        elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]').send_keys(mensagem)

    def send(driver):
        print('enviando a mensagem')
        time.sleep(20)
        elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
    
    def extract(driver):    
        mensagem = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/div[3]/div/div[1]/div[3]')
        mensagem=mensagem.get_attribute("outerHTML")
        soup=BeautifulSoup(mensagem,'html5lib')
        soup.get_text('!@#@!#@')

