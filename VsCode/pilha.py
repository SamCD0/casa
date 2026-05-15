pilha = []
print(type(pilha))
print()

print("inserindo paginas a pilha")
pilha.append("pagina1")
pilha.append("pagina2")
pilha.append("pagina3")
 
print("pilha atual:")
print(pilha)
print(f'Topo da pilha: {pilha[-1]}')
print()

print(f"Removendo paginas da pilha:")
print(pilha.pop())
print(pilha.pop())

print()
print("pilha atual:")
print(pilha)
