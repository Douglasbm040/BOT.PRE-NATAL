import pymysql

conexao = pymysql.connect(
    host = 'localhost',
    user='root',
    passwd='',
    database='db',




)

cursor=conexao.cursor()
cursor.execute('CREATE DATABASE comnursebot')
cursor.execute("SHOW TABLES")

for tabelas in cursor:
    print(tabelas)