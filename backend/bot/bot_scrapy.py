from bot_messenger import messenger
from bs4 import BeautifulSoup 
from firebase.firebase import db_firebase

#driver=messenger.driver



class scrapy:

    def extract():#driver):
        #print('realizando extraçao')    
        #elemento = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/div[3]/div/div[1]/div[3]')
        #mensagem= elemento.get_attribute("outerHTML")
        #soup=BeautifulSoup(mensagem,'html5lib')
        resposta={'conteudo':'1,2,3,4,5,6,7,8,9,0'}#soup.get_text(',')}
        obj_firestore=db_firebase.db
        soup=db_firesore.add_dados(obj_firestore,'resposta','7CPHGFP8B88u7Yqq5XhN',)
        return soup
        
    def organize_extract(soup):
        print('organizando !')


scrapy.extract() 

    

        
