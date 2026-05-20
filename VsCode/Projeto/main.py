from utils import titulo
from tarefas import adicionar_livro, listar_livros, atualizar_status, livros_ler, livros_concluidos, procurar_livro

def menu(): #mostra o menu/opções do ususario
    titulo("Sua biblioteca virtual")
    print("0 - sair")
    print("1 - adicionar livros")
    print("2 - listar livros")
    print("3 - atualizar status")
    print("4 - livros a ler")
    print("5 - livros concluidos")
    print("6 - procurar livro")

while True: #um loop que funciona até ser parado a força
    menu()
    escolha = input("Escolha uma opção: ") #<-,se for escolhido X, chama a função escolhida
    if escolha == "1":

        adicionar_livro()
    elif escolha == "2":

        listar_livros()
    elif escolha == "3":

        atualizar_status()
    elif escolha == "4":

        livros_ler()
    elif escolha == "5":

        livros_concluidos()
    elif escolha == "6":

        procurar_livro() 
    elif escolha == "0": #<- se esse for escolhido, encerra o funcionamento
        print("Tchau")
        break

