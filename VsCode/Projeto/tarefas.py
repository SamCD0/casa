from dados import livros, lidos, para_ler, status, prioridade
from utils import titulo

def adicionar_livro(): #<- função que permite adicionar  livros
    #define cada parte do livro
    titulo ("Adicionar Tarefa")
    titulos = input("Titulo do livro:")
    autor = input("Autor do livro:")
    ano = input("Ano de publicação:")
    genero = input("Gênero do livro:")
    prioridades = input("Prioridade (1. Baixa | 2. Média | 3. Alta): ")

    #mostra o processo de escolher a prioridade
    if prioridades == "1":
        prioridade = [0]
    elif prioridades == "2":
        prioridade = [1]
    elif prioridades == "3":
        prioridade = [2]
    #cria um dicionario com as informações
    dic_livros = {
        "id": len(livros) + 1,
        "tituloz": titulos,
        "autor": autor,
        "Ano_de_publicação": ano,
        "genero": genero,
        "prioridade": prioridades,
        "status": status[0]
    }
    #adiciona o livro as seguintes listas
    livros.append(dic_livros)
    para_ler.append(dic_livros)

    print("Livro cadastrado com sucesso.") 

def listar_livros(): #<- função que mostra os livros
        titulo("Listar livros")

        for i, livro in enumerate(livros, start=1): #lista os livros e suas informações
            print(f'Livro: {i}')
            print(f"id{livro['id']}")
            print(f"Titulo: {livro['tituloz']}")
            print(f"autor: {livro['autor']}")
            print(f"ano de publicação: {livro['Ano_de_publicação']}")
            print(f"genero: {livro['genero']}")
            print(f"Prioridade: {livro['prioridade']}")
            print(f"Status: {livro['status']}")
            print()  

def atualizar_status():#<- Função que deixa atualizar os dados do livro, pelo ID
    titulo("atualizar status")

    #verifica se tem livros cadastrados
    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return
    
    #se tem livros cadastrados, pede o ID do mesmo
    try:
        id_livro = int(input("Digite o ID da tarefa: "))
    except ValueError:
        print("Digite um número válido.")
        return
    
    #procura algum çivro com o ID colocado, e da as opções
    for livro in livros:
        if livro["id"] == id_livro:
            print("\nEscolha o novo status:")
            print("1 - Pendente")
            print("2 - Em andamento")
            print("3 - Concluída")
            escolha = input("Opção: ")

            #o que realmente muda o status, de acordo com o a escolha
            if escolha == "1":
                livro["status"] = status[0]
                if livro not in para_ler:
                    para_ler.append(livro)
            elif escolha == "2":
                livro["status"] = status[1]
                if livro in para_ler:
                    para_ler.remove(livro)
            elif escolha == "3":
                livro["status"] = status[2]
                if livro in para_ler:
                    para_ler.remove(livro)
                if livro not in lidos:
                    lidos.append(livro)
            else:
                print("Opção inválida.")
                return

            print("Status atualizado com sucesso!")#<-caso tudo de certo
            return

    print("Tarefa não encontrada.")#<- caso não tenha achado o id


def livros_ler(): #<- função que mostra os livros que ainda não foi iniciada a leitura
    titulo("Livros a Ler")

    if len(para_ler) == 0: #verifica os livros na lista para_ler
        print("Não há livros na fila para ler.")
        return

    for posicao, livro in enumerate(para_ler, start=1): #<-mostra os dados dos livros na lista para_ler, 
        print(f"Posição {posicao} na fila:")
        print(f"  ID: {livro['id']}")
        print(f"  Título: {livro['tituloz']}")
        print(f"  Autor: {livro['autor']}")
        print(f"  Ano: {livro['Ano_de_publicação']}")
        print(f"  Gênero: {livro['genero']}")
        print(f"  Prioridade: {livro['prioridade']}")
        print(f"  Status: {livro['status']}")
        print()


def livros_concluidos(): #<- este, procura da lista lidos, aqueles que já forma lidos
    titulo("Livros Concluídos")

    if len(lidos) == 0: #ve se tem livros na pilha
        print("Nenhum livro concluído.")
        return

    for posicao, livro in enumerate(reversed(lidos), start=1): #mostra os livros da lista lidos, pelo formato de pilha
        print(f"Posição {posicao} na lista de livros concluídos:")
        print(f"  ID: {livro['id']}")
        print(f"  Título: {livro['tituloz']}")
        print(f"  Autor: {livro['autor']}")
        print(f"  Ano: {livro['Ano_de_publicação']}")
        print(f"  Gênero: {livro['genero']}")
        print(f"  Prioridade: {livro['prioridade']}")
        print(f"  Status: {livro['status']}")
        print()


def procurar_livro(): #<-sistema de busca de livros
    titulo("Procurar Livro")
    procura = input("Digite o título ou autor: ").strip() #pede ao usuario informar o titulo/autor

    if procura == "":
         #ve se o usuario digitou algo
        print("Digite uma palavra de busca válido.")
        return

    procura = procura.lower() #deixa o que for escrito minusculo
    encontrados = [
        livro for livro in livros
        if procura in livro["tituloz"].lower() or procura in livro["autor"].lower()
    ]

    if len(encontrados) == 0: #se não achar livros, volta
        print("Nenhum livro encontrado para esse termo.")
        return

    for i, livro in enumerate(encontrados, start=1): # lista os livros encontrados e seus dados
        print(f"Resultado {i}:")
        print(f"  ID: {livro['id']}")
        print(f"  Título: {livro['tituloz']}")
        print(f"  Autor: {livro['autor']}")
        print(f"  Ano: {livro['Ano_de_publicação']}")
        print(f"  Gênero: {livro['genero']}")
        print(f"  Prioridade: {livro['prioridade']}")
        print(f"  Status: {livro['status']}")
        print()

