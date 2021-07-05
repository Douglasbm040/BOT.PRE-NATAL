from BOT_MESSENGER import bot

bot=bot.Bot_messenger
driver= bot.driver

def main():
     
     contact="É eu msm"
     link='https://web.whatsapp.com/'
     bot.on_marionette(link)
     bot.authentication(driver)
     bot.clear_box_contact(driver)
     bot.search_contact(contact,driver)
     bot.write('ola mundo',driver)
     bot.send(driver)

main()

