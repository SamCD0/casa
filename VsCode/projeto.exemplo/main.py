from dados import tarefas, fila_pendente, pilha_concluida, prioridades, status
from utils import titulo
from tarefas import cadastrar_tarefa, listar_tarefas, atualizar_status, ver_historico_concluidas


def mostrar_menu():
    titulo("Gerenciador de Tarefas")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Atualizar Status")
    print("4. Histórico de Tarefas Concluídas")
    print("5. Sair")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        
        cadastrar_tarefa()

    elif opcao == "2":
        
        listar_tarefas()

    elif opcao == "3":
        
        atualizar_status()

    elif opcao == "4":
        
        ver_historico_concluidas()

    elif opcao == "5":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")