def criar_rotina():
    print('Este bot foi desenvolvido para ajudar as gestante durante o prenatal')
    print('o programa é configurado por padrão a se iniciar automaticamente uma rotina que inicia as 15:22 de segunda a sexta')
    print('é necessária a autentificação da conta whatapp logo após a inicialização do programa ')
    input('aperte enter para iniciar rotina especificada')
    arquivo = open(r"C:\Users\dougl\Documents\GitHub\BOT.PRE-NATAL\project\agendador\agendador.bat", "w")
    arquivo.write('SCHTASKS /Create /SC weekly /D MON,TUE,WED,THU,FRI /TN nursebot-prenatal /ST 15:30 /TR C:\\Users\\dougl\\Documents\\GitHub\\BOT.PRE-NATAL\\project\\main\\main.exe')
    # schtasks /create /tn Security Script /tr sec.vbs /sc minute /mo 100 /st 17:00 /et 08:00 /k
    print('rotina programada com sucesso !')
criar_rotina()