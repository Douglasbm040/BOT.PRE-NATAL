from BOT_MESSENGER import bot

bot=bot.Bot_messenger


def main():
     driver=bot.driver
     contact="É eu msm"
     link='https://web.whatsapp.com/'
     bot.elemento
     bot.authentication(driver)
     bot.clear_box_contact(driver)
     bot.search_contact(contact,driver)
     bot.acess_contact(driver)
     bot.write('agora vai hehehehe',driver)
     bot.send(driver)

main()

