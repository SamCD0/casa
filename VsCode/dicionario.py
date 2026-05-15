aluno = {
    "nome": "Ana Lucia",
    "idade": 22,
    "curso": "Ciencia da  computação",
    "notas": [8.5, 9.0, 7.5]
}

print(aluno)

print(aluno["nome"])
print(aluno["idade"])

print("---Acesso seguro com get()---")
print(aluno.get("turma", "N/A"))
print(type(aluno))
