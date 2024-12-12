salario_funcionario = float(input('Qual é o salário do funcionário: R$'))

if salario_funcionario > 1250:
    aumento = salario_funcionario * 0.1
    novo_salario = salario_funcionario + aumento
    print(f'Quem ganhava R${salario_funcionario:.2f} com aumento de 10%, passa a ganhar R${novo_salario:.2f} agora.')
else:
    aumento = salario_funcionario * 0.15
    novo_salario = salario_funcionario + aumento
    print(f'Quem ganhava R${salario_funcionario:.2f} com aumento de 15%, passa a ganhar R${novo_salario:.2f} agora.')
