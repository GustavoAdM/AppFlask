import sqlite3
from bcrypt import hashpw, gensalt

creator = sqlite3.connect('ext/db/usuarios.db')

curso = creator.cursor()

curso.execute('''
    CREATE TABLE IF NOT EXISTS DadosLogin(
        id INTEGER NOT NULL PRIMARY KEY,
        usuario TEXT NOT NULL,
        email TEXT NOT NULL,
        senha TEXT NOT NULL
    );
''') 


def cadastrauser(usuario ,email, senha):
    with sqlite3.connect('ext/db/usuarios.db') as creator:
        curso = creator.cursor()
        hash = hashpw(senha.encode('utf-8'), gensalt(10))
        curso.execute('''
            INSERT INTO DadosLogin (usuario, email, senha ) VALUES(?, ?, ?)
        ''', (usuario, email, hash))
        creator.commit()


def excluiruser(id):
    curso.execute(f'''DELETE FROM DadosLogin WHERE id = {id}''')
    creator.commit()


def infoUser(sess):
    with sqlite3.connect('ext/db/usuarios.db') as creator:
        curso = creator.cursor()
        dados = curso.execute('''SELECT * FROM DadosLogin''').fetchall()
        
        for numdados in range(0, len(dados)):
            if sess == dados[numdados][2]:
                return dados[numdados][1]


def buscardados(email, senha):
    with sqlite3.connect('ext/db/usuarios.db') as creator:
        curso = creator.cursor()
        dados = curso.execute('''SELECT * FROM DadosLogin''').fetchall()
        
        for numdados in range(0, len(dados)):#contar a quantidade de usuarios
            if email in dados[numdados]: # verificar se tem o email no banco de dados
                hash = hashpw(senha.encode('utf-8'), dados[numdados][3]) 
                # verificar a senha, usando o hash do banco de dados, assim devolve o mesmo hash
                if dados[numdados][2] == email and dados[numdados][3] == hash:
                    return True, dados[numdados][1]
                else:
                    return False
            if numdados + 1 > len(dados):
                return 'Nao foi possivel encontrar'



curso.close()
