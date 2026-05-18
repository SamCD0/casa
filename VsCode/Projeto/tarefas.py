from dados import livros, sendo_lidos, lidos, para_ler, prioridade, status
from utils import titulo

def adicionar_livro():
    titulo ("Adicionar Tarefa")
    titulos = input("Titulo do livro:")
    autor = input("Autor do livro:")
    ano = input("Ano de publicação:")
    genero = input("Gênero do livro:")
    prioridades = input("Prioridade (1. Baixa | 2. Média | 3. Alta): ")

    if prioridades == "1":
        prioridade = [0]
    elif prioridades == "2":
        prioridade = [1]
    elif prioridades == "3":
        prioridade = [2]

    dic_livros = {
        "id": len(livros) + 1,
        "tituloz": titulos,
        "autor": autor,
        "Ano_de_publicação": ano,
        "genero": genero,
        "prioridade": prioridades,
        "status": status[0]
    }

    livros.append(dic_livros)
    sendo_lidos.append(dic_livros)

    print("Livro cadastrado com sucesso.")

def listar_livros():
        titulo("Listar livros")

        for i, livro in enumerate(livros, start=1):
            print(f'Livro: {i}')
            print(f"id{livro['id']}")
            print(f"Titulo: {livro['tituloz']}")
            print(f"autor: {livro['autor']}")
            print(f"ano de publicação: {livro['Ano_de_publicação']}")
            print(f"genero: {livro['genero']}")
            print(f"Prioridade: {livro['prioridade']}")
            print(f"Status: {livro['status']}")
            print()  

def atualizar_status():
    titulo("atualizar status")

    if len(livros) == 0:
        return
    
    try:
        id_livro = int(input("Digite o ID da tarefa: "))
    except ValueError:
        print("Digite um número válido.")
        return

    for livro in livros:
        if livro["id"] == id_livro:
            print("\nEscolha o novo status:")
            print("1 - Pendente")
            print("2 - Em andamento")
            print("3 - Concluída")
            escolha = input("Opção: ")

            if escolha == "1":
                    livro["status"] = status[0]
                    if livro not in para_ler:
                        para_ler.append(livro)
            elif escolha == "2":
                    livro["status"] = status[1]
            elif escolha == "3":
                    livro["status"] = status[2]
                    livro.append(lidos)   
            if livro in para_ler:
                    para_ler.append(livro)  

            print("Status atualizado com sucesso!")
            return

    print("Tarefa não encontrada.")

def ainda_ler():
    titulo("Livros ainda não iniciados")
    if para_ler != status[0]:
        print("Nenhum livro na fila.")
        return

    for i, livro in enumerate(para_ler, start=1):
        print(f"{i}. {livros}")