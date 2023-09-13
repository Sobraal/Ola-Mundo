salario = float(input('Qual é o salario do funcionario??'))
novo = salario + (salario * 15 / 100)
print ('Um funcionario que ganhava R$ {:.2f}, com 15% de aumento, passa areceber R${:.2f}' .format(salario, novo))