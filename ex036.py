#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprodor, e em quantos anos ele vai pagar.
#Calcule o valor mensal da prestação sabendo que ela não pode exceder 30% do salário ou ent]ao o empréstimo será negado.

from time import sleep
valor = float(input('Digite o valor da casa que você deseja comprar: R$ '))
salário = float(input('Digite o valor do seu salário atual: R$ '))
anos = int(input('Em quantos anos você deseja pagar a casa? '))
print('Vamos confirmar as informações digitadas...')
sleep(2)
print('O valor da casa que você seja comprar é de R$ {:2f}, seu salário atual é de R$ {:2f}, e você deseja quitar este financiamento em {} anos.'.format(valor, salário, anos))
sleep(4)
meses = (anos * 12)
print('Serão necessários {} meses para quitar este financiamento.'.format(meses))
sleep(3)
print('Agora vamos calcular qual será o valor mensal da prestação, para saber se é compatível com sua renda.')
sleep(3)
prestação = valor / meses
print('O valor da prestação será de R$ {:2f} mensais.'.format(prestação))
sleep(3)
mínimo = salário * 30 / 100 #30% do salário
print('Vamos analisar se o seu financiamento pode ser concedido.')
sleep(3)
print('Por favor, aguarde um momento.')
sleep(6)
if prestação <= mínimo:
    print('Parabéns! O empréstimo pode ser CONCEDIDO para financiar seu imóvel!')
else:
    print('Desculpe, infelizmente seu empréstimo será NEGADO. A prestação excede 30% do seu salário.')




