number = int(input('Digite um número para ver a sua tabuada: '))

print(15 * '-')
print(f'Tabuada de {number}')
for i in range(1, 11):
	resultado = number * i
	print(f'{number} x {i:2} = {resultado:2}')


print(15 * '-')
