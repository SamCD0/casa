from dados import livros, sendo_lidos, lidos, para_ler, prioridade, status
from utils import titulo
from tarefas import adicionar_livro, listar_livros, atualizar_status, ainda_ler

def menu():
    titulo("Sua biblioteca virtual")
    print("1 - adicionar livros")
    print("2 - listar livros")
    print("3 - atualizar status")
    print("4 - livros a ler")
    print("5 - livros concluidos")
    print("6 - procurar livro")

while True:
    menu()
    escolha = input("Escolha uma opção: ")
    if escolha == "1":

        adicionar_livro()
    elif escolha == "2":

        listar_livros()
    elif escolha == "3":

        atualizar_status()
    elif escolha == "4":

        ainda_ler()
        