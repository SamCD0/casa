cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Porto Alegre"]

cidades.append("Salvador")

cidades.insert(2, "Brasilia")

cidades.remove("Curitiba")
del cidades[3]

print(f'Cidades: {cidades}')