from bot import admin
from bot import bot_scrapy
import schedule
Bot= admin.admin_bot
scrapy = bot_scrapy.scrapy
def main():
     Bot.startbot()
     job=Bot.Bot_messenger('EU NAO SOU UM ROBOT','É eu msm')
     scrapy.extract()
     schedule.every().monday.do(job)   
main()



