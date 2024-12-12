nome_completo = input('Informe o seu nome completo: ')

print('Analisando o seu nome... ')
print(f'Seu nome em maiúsculas é {nome_completo.upper()}')
print(f'Seu nome em minúsculas é {nome_completo.lower()}')
print()

nome_completo_letras = nome_completo.replace(' ', '')
print(f'Seu nome ao todo {len(nome_completo_letras)} letras')
print()

dividido = nome_completo.split()
print(f'Seu primeiro nome é {dividido[0]} e ele tem {len(dividido[0])} letras')