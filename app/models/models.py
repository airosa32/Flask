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

    def ver (self, tabela, lista_campos = '*'):
        self.cursor.execute(f'select {lista_campos} from {tabela}')
        return self.cursor.fetchall()

    def consultar (self, tabela, lista_campo = '', lista_confere = ''):
        if lista_campo and lista_confere:
            self.cursor.execute(f'''select * from {tabela} where {lista_campo[0]}
            = '{lista_confere[0]}' and {lista_campo[1]} = '{lista_confere[1]}';''')
            return self.cursor.fetchall()

    def inserir (self, email = None, senha = None, string_lista = None):
        if string_lista:
            self.cursor.execute(f'insert into pessoas values {string_lista};')
            self.conect.commit() 
            return 'Dados inserido com sucesso'
        
        self.cursor.execute(f'''insert into pessoas values 
        ('{email}', '{senha}');''')
        self.conect.commit()

    def atualizar (self, tabela, atributo, valor_novo, campo, referencia):
        if type(valor_novo) == str:
            aspa = "'"

        self.cursor.execute(f'''update {self.database}.{tabela} 
        set {atributo} = {aspa}{valor_novo}{aspa} where ({campo} = '{referencia}');''')
        self.conect.commit() 
        return 'Dados atualizado com sucesso'

    def deletar (self, tabela, campo, referencia):
        self.cursor.execute(f'''delete from {self.database}.{tabela} 
        where ({campo} = '{referencia}');''')
        self.conect.commit() 
        return 'Dados deletados com sucesso'


#tiago = conexao(database='bd_teste')

#lista = "('stella@gmail.com', '1234'), ('sabrina', '123456')"
#print(tiago.inserir(string_lista=lista))
#print(tiago.ver('pessoas')[0][0])
#print(tiago.ver('pessoas',))
#print(tiago.consultar('pessoas', ['email', 'senha'], ['stella@gmail.com', '1234']))

#tiago.deletar('pessoas', 'email', 'sabrina')
#tiago.atualizar('pessoas', 'email', 'segundo_teste', 'email', 'terceiro_teste@gmail.com')