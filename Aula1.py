#Como variáveis seriam usadas em um programa real? 
#Problema 1 - Valor Por Hora
#Escreva um programa que retorna o valor hora de um funcionário com base no seu salário mensal e horas trabalhadas por mes
'''
input salario_mensal
input horas_trabalhadas_por_mes
valor_hora = salario_mensal/horas_trabalhadas_por_mes
print valor_hora
'''

salario_mensal = input('Qual é o seu salário mensal?')
horas_trabalhadas_por_mes = input('Quantas horas trabalha por mes?')
valor_hora = int (salario_mensal) / int (horas_trabalhadas_por_mes)
print (valor_hora)
