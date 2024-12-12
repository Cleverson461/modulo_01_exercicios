nome_completo = str(input('Informe o seu nome completo: ')).strip()

dividido = nome_completo.split()
print()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é = {dividido[0]}')
print(f'Seu último nome é = {dividido[-1]}')