from bot.bot_messenger import messenger
import time
robot= messenger
driver=robot.driver
class admin_bot:
    def perssistencia(func):
         while True:
            time.sleep(5) 
            try :
                func
                go=True

            except:
                go=False
                print(0)
                

            if go==True:
                break

    def startbot():
        robot.elemento
        robot.authentication(driver)

    def Bot_messenger(list_messenger,list_contact):    
        robot.click_box_contact(driver)            
        robot.clear_box_contact(driver)
        robot.search_contact(list_contact,driver)
        robot.acess_contact(driver)
        #robot.clear_box_text(driver)
        robot.write_box_text(list_messenger,driver)
        robot.send(driver)



    
    
        


