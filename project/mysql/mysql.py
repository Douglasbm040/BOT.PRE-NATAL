import pymysql

conexao = pymysql.connect(
    host = 'localhost',
    user='root',
    passwd='',
    database='nursebot.db',



)

cursor=conexao.cursor()
#cursor.execute('CREATE TABLE comcontato(nome VARCHAR(255),mensagem VARCHAR(255)) ')
cursor.execute("SHOW TABLES")

for tabelas in cursor:
    print(tabelas)