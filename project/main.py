from bot import admin
Bot= admin.admin_bot

def main():
     rodadas_de_testes=range(1,21)
     for i in rodadas_de_testes: 
          print(i,' rodada')
          Bot.startbot()
          Bot.Bot_messenger('EU NAO SOU UM ROBOT','É eu msm')
     
main()

