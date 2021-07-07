#importação
from selenium.webdriver.common.keys import Keys
from selenium import webdriver #importe do selenium webdriver "controlador" de site
from selenium.webdriver.firefox.options import Options #import do controlador especifico do firefox
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import time #biblioteca para adicionar um tempo de espera 
from bs4 import BeautifulSoup #manipular html




class messenger:
    link='https://web.whatsapp.com/'
    options = Options()
    options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
    driver = webdriver.Firefox(options=options, executable_path="C:/Users/dougl/Desktop/Nova pasta/geckodriver-v0.29.1-win64/2/geckodriver.exe")#adiconando o caminho do controlador de navegador
    elemento=driver.get(link)

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

    def click_box_contact(driver ):
        print('clicando no box contact')
        while True:

            
            try :
                elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[3]/div/header/div[2]/div/span/div[2]/div/span').click()
                go=True

            except:
                go=False
                

            if go==True:
                print('box clicado')
                break
    def clear_box_contact(driver):
        #print('limpando caixa de busca de contato')
        print('limpando no box contact')
        while True:
            try :
                elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[1]/div/label/div/div[2]').clear()
        
                go=True

            except:
                go=False
                
                

            if go==True:
                print('box contact limpo')
                break

    def search_contact(list_contact,driver):
        #print('digitando nome do contato')
        #time.sleep(20)
        print('pesquisando contact')
        while True:
            try :
                elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[1]/div/label/div/div[2]').send_keys(list_contact)
        
                go=True

            except:
                go=False
                
                

            if go==True:
                print('contact pesquisado')
                break
    def acess_contact(driver):
        #print('acessando contato ')
        time.sleep(15)                          #/html/body/div/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[2]/div[1]/div/div/div[2]/div/div
        print('acessando contato')
        while True:
            try :
                elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[2]/div[1]/div/div/div[2]/div/div/div[2]').click()
        
                go=True

            except:
                
                go=False
                
                

            if go==True:
                print('contado acessado')
                break
    def clear_box_text(list_messenger,driver):
        #print('limpando caixa de texto')
        #time.sleep(10)
        print('limpando box de texto')
        while True:
            try :
                elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]').clear() 
    
                go=True

            except:
                go=False
                
                

            if go==True:
                print('box de texto limpo')
                break    
    def write_box_text(list_messenger,driver):
        #print('escrevendo para o contato')
        #time.sleep(20)
        print('escrevendo mensagem')
        while True:
            try :
                elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]').send_keys(list_messenger)
        
                go=True

            except:
                go=False
                

            if go==True:
                print('mensagem escrita')
                break  
    def send(driver):
        #print('enviando a mensagem')
        #time.sleep(20)
        print('enviando mensagem')
        while True:
            try :
                elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)

                go=True

            except:
                go=False
                
                

            if go==True:
                print('mensagem enviada !')
                break 
    def extract():    
        mensagem = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/div[3]/div/div[1]/div[3]')
        mensagem=mensagem.get_attribute("outerHTML")
        soup=BeautifulSoup(mensagem,'html5lib')
        soup.get_text('!@#@!#@')

