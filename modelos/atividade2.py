#questão 1
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f"Carro: {self.modelo}, Cor: {self.cor}, Ano: {self.ano}"

carro_1 = Carro('Augi', 'Preto', 2023)
print(carro_1)

#questão 2
class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.menu = None
        self.mesas = 0

#questão 4
    def __str__(self):
        return f"Restaurante: {self.nome}, Categoria: {self.categoria}, Ativo: {self.ativo}, Menu: {self.menu}, Mesas: {self.mesas}"
    
#questão 3
restaurante1 = Restaurante('Praça', 'Gourmet')
restaurante1.endereco = 'Rua das Codornas, 145'
restaurante1.capacidade = 100
print(restaurante1)
#construtor
restaurante2 = Restaurante('La Rocca', 'Italiana')
print(restaurante2)

#questão 5
class Cliente:
    def __init__(self, nome, email, telefone, endereco):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    def __str__(self):
        return f"Cliente: {self.nome}, Email: {self.email}, Telefone: {self.telefone}, Endereço: {self.endereco}"

cliente1 = Cliente('Pedro Brecher', 'pedro.brecher@escola.pr.gov.br', '9258-7852', 'Rua Bom Jesus, 223')
cliente2 = Cliente('Heloise de Castro', 'heloise.castro@escola.pr.gov.br', '9568-4562', 'Rua Beija Flor, 78')
cliente3 = Cliente('Leticia Rompava', 'leticia.rompava@escola.pr.gov.br', '9984-2598', 'Rua Ouro Verde, 45')

print(cliente1)
print(cliente2)
print(cliente3)