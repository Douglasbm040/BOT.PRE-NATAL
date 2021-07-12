def criar_rotina():
    texto=input('nome de adminstrador: ')
    arquivo = open(r"C:\Users\dougl\Documents\GitHub\BOT.PRE-NATAL\project\agendador\agendador.bat", "a")
    arquivo.write('schtasks /create /tn agendamento_do_bot /tr ' + 'C:\\Users\\dougl\\Documents\\GitHub\\BOT.PRE-NATAL\\project\\main\\main.exe' + '/sc minutos' + '/mo 1'+ '/st 13:10'+'/et 13:01'+'/k')
    # schtasks /create /tn Security Script /tr sec.vbs /sc minute /mo 100 /st 17:00 /et 08:00 /k
    print(arquivo)
criar_rotina()