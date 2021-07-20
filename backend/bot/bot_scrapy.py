from bot.bot_messenger import messenger
from bs4 import BeautifulSoup 

driver=messenger.driver


class scrapy:

    def extract():
        print('realizando extraçao')    
        elemento = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/div[3]/div/div[1]/div[3]')
        mensagem= elemento.get_attribute("outerHTML")
        soup=BeautifulSoup(mensagem,'html5lib')
        print(soup.get_text(','))
        return soup
        
    def organize_extract(soup):
        print('')

        
