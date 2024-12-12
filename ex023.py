# Entrada do número
numero = int(input("Digite um número entre 0 e 9999: "))

# Verificação para garantir que o número está no intervalo
if 0 <= numero <= 9999:
    # Extração dos dígitos usando operações matemáticas
    unidade = (numero // 1) % 10
    dezena = (numero // 10) % 10
    centena = (numero // 100) % 10
    milhar = (numero // 1000) % 10

    # Exibição dos resultados
    print(f"Unidade: {unidade}")
    print(f"Dezena: {dezena}")
    print(f"Centena: {centena}")
    print(f"Milhar: {milhar}")
else:
    print("Número fora do intervalo permitido! Por favor, digite um número entre 0 e 9999.")
