# Entrada do nome da cidade
nome = input("Digite o nome da cidade: ").strip().lower()  # Remove espaços extras no início e no final

silva = 'silva' in nome

# Verifica se a cidade começa com "Santo"
if silva == True:  # Verifica os primeiros 5 caracteres, ignorando maiúsculas/minúsculas
    print("O nome 'Silva' está no nome")
else:
    print("O nome 'Silva' não está no nome")
