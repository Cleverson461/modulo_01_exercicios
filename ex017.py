# import math  # Importamos a biblioteca math para usar a função de raiz quadrada.

# # Entrada dos valores dos catetos
# cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
# cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

# # Cálculo da hipotenusa usando o Teorema de Pitágoras
# hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)

# # Exibição do resultado
# print(f"A hipotenusa do triângulo retângulo é: {hipotenusa:.2f}")

from math import hypot
co = float(input("Digite o comprimento do cateto oposto: "))
ca = float(input("Digite o comprimento do cateto adjacente: "))
hi = hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}')