from BOT_MESSENGER import bot

bot=bot.Bot_messenger

def main():
     contact="É eu msm"
     link='https://web.whatsapp.com/'
     bot.on_marionette()
     bot.acess(link)
     bot.authentication()
     bot.clear_box_contact()
     bot.search_contact(contact)
     bot.write('ola mundo')
     bot.send()

main()

