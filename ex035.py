# Programa para verificar se três retas podem formar um triângulo
print(30 * '-=')
print('Analisador de Triângulos')
print(30 * '-=')
print()

# Entrada dos comprimentos das três retas
reta1 = float(input("Digite o comprimento da primeira reta: "))
reta2 = float(input("Digite o comprimento da segunda reta: "))
reta3 = float(input("Digite o comprimento da terceira reta: "))
print()

# Verificação usando a condição de existência de um triângulo
if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
    print("Os segmentos acima PODEM FORMAR triângulo.")
else:
    print("Os segmentos acima NÃO PODEM FORMAR triângulo.")