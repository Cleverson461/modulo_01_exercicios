velocidade = float(input('Qual a velocidade atual do carro? '))
multa = (velocidade - 80) * 7.00

if velocidade > 80:
	print(f'MULTADO! Você excedeu o limite permitdio que é de 80km/h')
	print(f'Você deve pagar uma multa de R${multa}')
	print('Tenha um bom dia! Dirija com segunrança!')
else:
	print('Tenha um bom dia! Dirija com segunrança!')
	print(f'Parabéns continue assim, andando na velocidade permitida 80km/h')