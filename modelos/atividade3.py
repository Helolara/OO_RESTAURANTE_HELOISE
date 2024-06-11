# Atividade 1
class Pessoa:
    def __init__(self,nome, idade,profissao):
       self.nome=nome
       self.idade=idade
       self.profissao=profissao
    
    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Profissão: {self.profissao}"

    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
        return f"Saudação, me chamo {self.nome}, e trabalho como {self.profissao}."
    
pessoa1 = Pessoa("Karen", 27+1, "Médica")
print(pessoa1)              
pessoa1.aniversario()         
print(pessoa1.saudacao)    

# Atividade 2
class ContaBancaria:
    def __init__(self,titular,saldo,ativo,profissao,idade):
        self.titular=titular
        self.saldo=saldo
        self.ativo=False
        self.profissao=profissao
        self.idade=idade
        
# Atividade 3
    def __str__(self):
        return f'{self.titular} | {self.saldo} | {self.ativo} | {self.profissao} | {self.idade}'
    
# Atividade 4  
    @classmethod
    def ativar_conta(self):
        self.ativo=True

conta_titular=ContaBancaria('Antonio','R$45.000',True,'Tecnico de segurança',54)
conta_titular.ativar_conta()
print(conta_titular)

# Atividade 5
class ContaBancaria:
    def __init__(self, titular, saldo=0, ativo=False, profissao=None, idade=None):
        self.titular = titular
        self.saldo = saldo
        self.ativo = ativo
        self.profissao = profissao
        self.idade = idade

    @classmethod
    def ativar_conta(cls, conta):
        conta.ativo = True

# Atividade 6
conta = ContaBancaria('Lara', 10000)
print(conta.titular)

# Atividade 7
class ClienteBanco:
    def __init__(self, nome, saldo, ativo, profissao, idade):
        self.nome = nome
        self.saldo = saldo
        self.ativo = ativo
        self.profissao = profissao
        self.idade = idade

cliente1 = ClienteBanco('Henrique', 7000, True, 'Médico', 26)
cliente2 = ClienteBanco('Beatriz', 11000, False, 'Engenheira', 35)
cliente3 = ClienteBanco('Davi', 2000, True, 'Professor', 19)

# Atividade 8
@classmethod
def descricao_conta(cls):
    return f'Cliente: {cls.nome}, Saldo: {cls.saldo}, Ativo: {cls.ativo}, Profissão: {cls.profissao}, Idade: {cls.idade}'

ClienteBanco.descricao_conta = descricao_conta