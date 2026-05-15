from collections import deque
filla = deque()

filla.append("cliente A")
filla.append("cliente B")
filla.append("cliente C")

print("Fila atual:")
print(filla)
print()
print(f"Removendo o final da filla: {filla.popleft()}")
print("Fila atual:")
print(filla)