#importação
from selenium.webdriver.common.keys import Keys
from selenium import webdriver #importe do selenium webdriver "controlador" de site
from selenium.webdriver.firefox.options import Options #import do controlador especifico do firefox
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import time #biblioteca para adicionar um tempo de espera 
from bs4 import BeautifulSoup #manipular html
import pandas as pd #criar 'tabela'
from bs4 import BeautifulSoup

options = Options()# instancinado 
options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"#adicionando o caminho do navagado ao codigo
driver = webdriver.Firefox(options=options, executable_path="C:/Users/dougl/bin/geckodriver.exe")#adiconando o caminho do controlador de navegador


class bot_messenger:
    x='https://web.whatsapp.com/'
    contact="É eu msm"
    element=driver.get(x)
    time.sleep(20)

    def clear():
        elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[3]/div/header/div[2]/div/span/div[2]/div/span').click()
        time.sleep(20)
        print('limpando')
        elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[1]/div/label/div/div[2]').clear() 

    def search_contact():
        print('escrever')
        time.sleep(20)
        elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[1]/div/label/div/div[2]').send_keys(contact)

    def acess_contact():
        print('acessando')
        time.sleep(10)
        elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/span').click()

    def write():
        print('limpando')
        elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]').clear() 
        print('escrever')
        time.sleep(20)
        elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]').send_keys('hello world, eu sou um robo')

    def send():
        print('acessando')
        time.sleep(20)
        elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)

def extract():
    mensagem = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/div[3]/div/div[1]/div[3]')
    mensagem=mensagem.get_attribute("outerHTML")
    soup=BeautifulSoup(mensagem,'html5lib')
    soup.get_text('!@#@!#@')
#DIA
