import math  # Importamos a biblioteca math para realizar os cálculos trigonométricos.

# Entrada do ângulo em graus
angulo = float(input("Digite o ângulo em graus: "))

# Cálculos
seno = math.sin(math.radians(angulo))  # Calcula o seno
cosseno = math.cos(math.radians(angulo))  # Calcula o cosseno
tangente = math.tan(math.radians(angulo))  # Calcula a tangente

# Exibição dos resultados
print(f"O ângulo de {angulo} graus tem:")
print(f"Seno: {seno:.2f}")
print(f"Cosseno: {cosseno:.2f}")
print(f"Tangente: {tangente:.2f}")
