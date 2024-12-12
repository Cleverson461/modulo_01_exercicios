import random  # Importamos a biblioteca random para realizar o sorteio.

# Entrada dos nomes dos alunos
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

# Colocamos os nomes em uma lista
alunos = [aluno1, aluno2, aluno3, aluno4]

# Embaralhamos a lista aleatoriamente
random.shuffle(alunos)

# Exibição da ordem sorteada
print("A ordem de apresentação será:")
for i, aluno in enumerate(alunos, start=1):
    print(f"{i}º - {aluno}")
