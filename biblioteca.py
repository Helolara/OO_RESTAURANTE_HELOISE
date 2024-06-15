#Questão 5 e 6 e 7
from atividade4 import Livro

livro1 = Livro("Beleza Negra", "Anna Sewell", 1877) 
livro2 = Livro("O Senhor dos Anéis", "J. R. R. Tolkien", 1954)

livro1.emprestar()

print(f"O livro 'O Pequeno Príncipe' está disponível após o empréstimo? {'Sim' if livro1.disponivel else 'Não'}")

livros_disponiveis_1999 = Livro.verificar_disponibilidade(1999)
for livro in livros_disponiveis_1999:
    print(livro)

livros_disponiveis_1954 = Livro.verificar_disponibilidade(1954)
for livro in livros_disponiveis_1954:
    print(livro)