usuarios = []
relatorios = []

class Conta():
    def __init__(self, Codigo, senha, nome, tipo):
        self.Codigo = Codigo
        self.senha = senha
        self.nome = nome
        self.tipo = tipo
    
    def __str__(self):
         return f"Codigo: {self.Codigo}, Nome: {self.nome}, Senha: {self.senha}, Tipo: {self.tipo}"
     
class RelatorioDeManipulacao():
    def __init__(self, Setor, Data, Hora, Codigo, Nome):
        self.Setor = Setor
        self.Data = Data
        self.Hora = Hora
        self.Codigo = Codigo
        self.Nome = Nome
    
    def __str__(self):
        return f'Setor Movimentado: {self.Setor}, Data: {self.Data}, Hora: {self.Hora}, Codigo: {self.Codigo}, Funcionario: {self.Nome}'
     
def verificarSenha(senha):
    if len(senha) < 6:
        print("A senha tem que ser maior que 6 digitos!")
        return False
    elif senha < 0:
        print("A senha n pode ser menor que 0!")
        return False
    elif senha.isdigit() == False:
        print("A senha deve ser apenas de numeros!")
        return False
    else:
        return True
    
    
def criarConta():
    from random import randint as r
    from datetime import date, datetime
    import time
    import sqlite3 as sql
    
    conect = sql.connect("bancoDeDados.db")
    cursor = conect.cursor()
    
    codigo = r(1000, 9999)
    nome = input("Nome de usuario: ")
    senha = input("Crie uma senha: ")
    
    while(True):
        comando = f"select Codigo from USUARIOS"
        cursor.execute(comando)
        conect.commit()
        linhas = cursor.fetchall()
    
        if codigo in  linhas:
            continue
        else:
            break
    
    comando = f"insert into usuarios VALUES({int(codigo)}, '{nome}', {int(senha)}, 'Cliente');"
    cursor.execute(comando)
    conect.commit()
        
    comand2 = f"select * from usuarios;"
    cursor.execute(comand2)
    conect.commit()
    linhas = cursor.fetchall()
    
    CodigoEmpregado = codigo
    print (type(CodigoEmpregado))
    print (type(codigo))
    
    for Codigo, Nome, senha, Tipo in linhas:
        conta = Conta(Codigo, senha, Nome, Tipo)
        usuarios.append(conta)
        print (type(codigo))
        
        if CodigoEmpregado == Codigo:
            relatorios.append(RelatorioDeManipulacao('Cadastro', date.today().strftime('%d/%m/%Y'), datetime.now().strftime('%H:%M'), conta.Codigo, conta.nome))

    cursor.close()
    conect.close()
        
criarConta()

for contas in usuarios:
    print(contas)

for relatorio in relatorios:
    print (relatorio)