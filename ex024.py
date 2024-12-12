# Entrada do nome da cidade
cidade = input("Digite o nome da cidade: ").strip()  # Remove espaços extras no início e no final

# Verifica se a cidade começa com "Santo"
if cidade[:5].upper() == "SANTO":  # Verifica os primeiros 5 caracteres, ignorando maiúsculas/minúsculas
    print("O nome da cidade começa com 'Santo'.")
else:
    print("O nome da cidade não começa com 'Santo'.")
