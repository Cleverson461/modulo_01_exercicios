# Entrada da frase
frase = str(input("Digite uma frase: ")).strip().upper()  # Remove espaços extras e converte para minúsculas

# Conta o número de vezes que a letra 'a' aparece
quantidade_a = frase.count('A')
print(f"A letra 'A' aparece {quantidade_a} vezes na frase.")

# Encontra a posição da primeira ocorrência da letra 'a'
primeira_posicao = frase.find('A') + 1  # Adiciona 1 para ajustar à numeração humana
print(f"A primeira ocorrência da letra 'A' está na posição {primeira_posicao}.")

# Encontra a posição da última ocorrência da letra 'a'
ultima_posicao = frase.rfind('A') + 1  # Adiciona 1 para ajustar à numeração humana
print(f"A última ocorrência da letra 'A' está na posição {ultima_posicao}.")