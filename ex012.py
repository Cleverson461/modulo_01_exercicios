preco = float(input('Informe o preço do produto? R$'))
desconto = preco * 0.05
novo_preco = preco - desconto

print(f'Valor original:     R${preco:.2f}')
print(f'Valor com desconto: R${novo_preco:.2f}')
print(f'O produto que custava R${preco:.2f}, na promoção com desconto de 5% vai custar R${novo_preco:.2f}')