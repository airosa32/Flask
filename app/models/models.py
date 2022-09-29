import mysql.connector as msql

class conexao():
    def __init__(self, host = 'localhost', user = 'root',
    password = '', database = ''):
        self.database = database
        self.conect = msql.connect (
            host = host,
            user = user,
            password = password,
            database = database)
        self.cursor = self.conect.cursor()

    def sair (self):  
        self.cursor.close()                 
        self.conect.close()

    def ver (self, tabela):
        self.cursor.execute(f'select * from {tabela}')
        return self.cursor.fetchall()

    def inserir (self, email = None, senha = None, string_lista = None):
        if string_lista:
            self.cursor.execute(f'insert into pessoas values {string_lista};')
            self.conect.commit() 
            return 'Dados inserido com sucesso'
        
        self.cursor.execute(f'''insert into pessoas values 
        ('{email}', '{senha}');''')
        self.conect.commit()

    def atualizar (self, tabela,  campo, referencia, atributo, valor_novo):
        self.cursor.execute(f'''update {self.database}.{tabela} 
        set {atributo} = '{valor_novo}' where ({campo} = '{referencia}');''')
        self.conect.commit() 
        return 'Dados atualizado com sucesso'

    def deletar (self, tabela, campo, referencia):
        self.cursor.execute(f'''delete from {self.database}.{tabela} 
        where ({campo} = '{referencia}');''')
        self.conect.commit() 
        return 'Dados deletados com sucesso'


#tiago = conexao(database='bd_teste')

#lista = '''('stella@gmail.com', '1234'), ('sabrina', '123456')'''
#print(tiago.inserir(string_lista=lista))
#print(tiago.ver('pessoas'))

#tiago.deletar('pessoas', 'email', 'sabrina')
#tiago.atualizar('pessoas', 'email', 'segundo_teste', 'email', 'terceiro_teste@gmail.com')