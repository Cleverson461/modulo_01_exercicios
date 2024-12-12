import random  # Importamos a biblioteca random para realizar o sorteio.

# Entrada dos nomes dos alunos
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

# Colocamos os nomes em uma lista
alunos = [aluno1, aluno2, aluno3, aluno4]

# Sorteamos um nome aleatoriamente
escolhido = random.choice(alunos)

# Exibição do resultado
print(f"O aluno escolhido para apagar o quadro foi: {escolhido}")
