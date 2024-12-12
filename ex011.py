largura_da_parede = float(input('Informe a largura da parede: '))
altura_da_parede = float(input('Informe a altura da parede: '))
area = altura_da_parede * largura_da_parede

print(f"Sua parede tem a dimensào de {largura_da_parede}x{altura_da_parede} e suaa área é de {area:.2f}m².")


litro_de_tinta = area / 2
print(f"Você precisará de {litro_de_tinta:.2f} litros de tinta para pintá-la.")