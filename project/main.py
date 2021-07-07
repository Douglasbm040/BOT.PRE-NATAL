from bot import admin
Bot= admin.admin_bot

def main():
     for i in range(1,21): 
          print(i,' rodada')
          Bot.startbot()
          Bot.Bot_messenger('EU NAO SOU UM ROBOT','É eu msm')
     
main()

