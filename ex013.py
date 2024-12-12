salario = float(input('Qual é o salário do Funcionário? R$'))
salario_com_porcentagem = salario * 0.15
novo_salario = salario + salario_com_porcentagem

print(f'Um funcionário que ganhava R${salario:.2f},  com aumento de 15%, passa a receber R${novo_salario:.2f}')