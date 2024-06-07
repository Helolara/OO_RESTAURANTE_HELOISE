# Classe Carro
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f"Carro: {self.modelo}, Cor: {self.cor}, Ano: {self.ano}"

# Criando uma instância da classe Carro
carro1 = Carro('Augi', 'Preto', 2023) 
print(carro1)

# Classe Restaurante
class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.endereco = None
        self.capacidade = 100 

    def __str__(self):
        return f"Restaurante: {self.nome}, Categoria: {self.categoria}, Ativo: {self.ativo}, Endereço: {self.endereco}, Capacidade: {self.capacidade}"

# Criando uma instância da classe Restaurante e atribuindo valores aos seus atributos
restaurante1 = Restaurante('Praça', 'Gourmet')
restaurante1.endereco = 'Rua das Codornas, 165'
restaurante1.capacidade = 100
print(restaurante1)

# Criando uma instância da classe Restaurante utilizando o construtor
restaurante2 = Restaurante('La Rocca', 'Italiana')
print(restaurante2)

# Classe Cliente
class Cliente:
    def __init__(self, nome, email, telefone, endereco):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    def __str__(self):
        return f"Cliente: {self.nome}, Email: {self.email}, Telefone: {self.telefone}, Endereço: {self.endereco}"

# Instanciando 3 objetos da classe Cliente e atribuindo valores aos seus atributos
cliente1 = Cliente('João Lara', 'joaolara@gmail.com', '9958-1254', 'Rua Bom Jesus, 789')
cliente2 = Cliente('Rosane Maria', 'rosanemaria@gmail.com', '8956-521', 'Rua Beija-flor, 125')
cliente3 = Cliente('Gabriel Castro', 'gabrielcastro@gmail.com', '9887-4562', 'Rua Ouro Verde, 236')

print(cliente1)
print(cliente2)
print(cliente3) 
