from dados import tarefas, prioridades, status, fila_pendente, pilha_concluida
from utils import titulo

def cadastrar_tarefa():
    titulo("Cadastrar Tarefa")

    decricao     = input("Descrição: ")
    disciplina   = input("Disciplina: ")
    data_entrega = input("Data (DD/MM/AA): ")

    print(' - Prioridades: 1. Baixa | 2. Média | 3. Alta')
    opcao = input("Prioridade: ")

    # Lê a prioridade da tupla pelo índice
    if opcao == "1":
        prioridade = prioridades[0]  # "Baixa"
    elif opcao == "2":
        prioridade = prioridades[1]  # "Média"
    else:
        prioridade = prioridades[2]  # "Alta"

    # Cria o dicionário representando a tarefa
    dict_tarefa = {
        "id":           len(tarefas) + 1,
        "decricao":     decricao,
        "disciplina":   disciplina,
        "data_entrega": data_entrega,
        "prioridade":   prioridade,
        "status":       status[0]  # sempre "Pendente"
    }

    tarefas.append(dict_tarefa)        # adiciona à lista principal
    fila_pendente.append(dict_tarefa)  # adiciona à fila de pendentes (FIFO)

    print("Tarefa cadastrada com sucesso!")

def listar_tarefas():
     titulo("Listar Tarefas")

     for i, tarefa in enumerate(tarefas, start=1):
        print(f'TAREFA: {i}')
        print(f"ID: {tarefa['id']}")
        print(f"Descrição: {tarefa['decricao']}")
        print(f"Disciplina: {tarefa['disciplina']}")
        print(f"Data de Entrega: {tarefa['data_entrega']}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Status: {tarefa['status']}")
        print()  
    
def atualizar_status():
    print("\n--- Atualizar Status ---")
    listar_tarefas()

    # Guarda 1: lista vazia — nada a atualizar
    if len(tarefas) == 0:
        return

    # Guarda 2: usuário pode digitar texto em vez de número
    try:
        id_tarefa = int(input("Digite o ID da tarefa: "))
    except ValueError:
        print("Digite um número válido.")
        return

    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            print("\nEscolha o novo status:")
            print("1 - Pendente")
            print("2 - Em andamento")
            print("3 - Concluída")
            opcao = input("Opção: ")

            if opcao == "1":
                tarefa["status"] = status[0]
                if tarefa not in fila_pendente:
                    fila_pendente.append(tarefa)
            elif opcao == "2":
                tarefa["status"] = status[1]
            elif opcao == "3":
                tarefa["status"] = status[2]
                pilha_concluida.append(tarefa)   # empilha!
                if tarefa in fila_pendente:
                    fila_pendente.remove(tarefa)  # sai da fila

            print("Status atualizado com sucesso!")
            return

    print("Tarefa não encontrada.")

def ver_historico_concluidas():
    titulo("Histórico de Tarefas Concluídas")
    if len(pilha_concluida) == 0:
        print("Nenhuma tarefa concluída.")
    else:
        print(f"Total de tarefas concluídas: {len(pilha_concluida)}\n")
    

    # reversed() percorre do TOPO para a BASE
    # = mais recente primeiro (comportamento LIFO)
    for i, tarefa in enumerate(reversed(pilha_concluida), start=1):
        print(f'TAREFA CONCLUÍDA: {i}')
        print(f"ID: {tarefa['id']}")
        print(f"Descrição: {tarefa['decricao']}")
        print(f"Disciplina: {tarefa['disciplina']}")
        print(f"Data de Entrega: {tarefa['data_entrega']}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print()