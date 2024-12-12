medida = float(input('Digite o tamanho do metro: '))
decimetro = medida * 10
centrimetro = medida * 100
milimetro = medida * 1000
kilometro = medida / 1000
hectometro = medida / 100
decametro = medida / 10

print(f'A medida de {medida}m corresponde a {decimetro:.0f}dm')
print(f'A medida de {medida}m corresponde a {centrimetro:.0f}cm')
print(f'A medida de {medida}m corresponde a {milimetro:.0f}mm')
print(f'A medida de {medida}m corresponde a {kilometro}km')
print(f'A medida de {medida}m corresponde a {hectometro}hm')
print(f'A medida de {medida}m corresponde a {decametro}dam')