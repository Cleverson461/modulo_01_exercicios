num1 = int(input('Informe um número: '))
num2 = int(input('Informe um segundo número: '))
num3 = int(input('Informe um terceiro número: '))

# Verificando quem é menor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
elif num3 < num1 and num3 < num2:
    menor = num3

# Verificando quem é maior
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
elif num3 > num1 and num3 > num2:
    maior = num3

print()
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
