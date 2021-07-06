from bot.bot_messenger import messenger

robot= messenger

class admin_bot:
    
    driver=robot.driver

    def startbot():
        robot.elemento
        robot.authentication(driver)

    def Bot_messenger(list_messenger,list_contact):
        for i in list_messenger:
            
            robot.clear_box_contact(driver)
            robot.search_contact(list_contact,driver)
            robot.acess_contact(driver)
            robot.write(list_messenger,driver)
            robot.send(driver)

