print('========================= 05 ANTERCESSOR SUCESSOR ===============================')

n = int(input('Digite um numero: '))
a = n - 1
s = n + 1
print('analisando Seu numero: {} seu antercessor é: {} e seu sucessor é {}'.format(n,a,s))

print('========================= 06 DOBRO TRIPLO QUADRADO ===============================')

num = int(input('Digite um numero: '))
d = num * 2
t = num * 3
r = num * num
print('analisando seu numero: {} seu dobro é: {} seu triplo é: {} e ao quadrado é {}'.format(num,d,t,r))

print('========================= 07 MEDIA DO ALINO ===============================')

nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a Segunda nota: '))
nota3 = int(input('Digite a terceira nota: '))
result = (nota1+nota2+nota3)/3
print('Analisando os valores incluidos acima a sua média é: {}'.format(result))

print('========================= 08 CONVERTER METRO CENTIMETRO E MILIMETRO ===============================')

medida = float(input('Digite o valor em metro: '))
cen = medida*100
mil = medida*1000
print('você digitou: {} metro(s), seu centimetro é de: {} e seu milimetro de: {}'.format(medida,cen,mil))

print('========================= 09 TABUADA EM WHILE ===============================')

tab = int(input('Digite um numero inteiro e veja sua tabuada: '))
aux = 0
print('*' * 18)
print('Tabuada de {}'.format(tab))
print('*' * 18)
while(aux <= 10):
    print('{} x {} = {}'.format(aux,tab, (aux * tab)))
    aux = aux + 1

print('========================= 10 REAL EM DOLAR ===============================')

valor = float(input('Quantos Reais você quer converter para Dolar? '))
print('Cotação do Dolár está em U$ 1.00 = R$ 5.30')
us = valor / 5.30
print('com R${} você consegue U${:.2f}'.format(valor,us))

print('========================= 11 METRO QUADRADO EM TINTA ===============================')

altura = float(input('Digite o Altura da parede que você irá pintar: '))
largura = float(input('Digite a largura da parede que você irá pintar: '))
area = altura*largura
tinta = area / 2
print('a area em m2 é {} e você irá precisar de {} Litros de tinta para pintar sua parede'.format(area,tinta))

print('========================= 12 DESCONTOS DE UM PREÇO ===============================')

valor_original = float(input('O valor original: R$ '))
print('valor original: R$',valor_original)
print('Desconto ganho: R$',valor_original * 0.05)
print('Valor com desconto: R$',valor_original * 0.95)

print('========================= 13 AUMENTO DE SALARIO 15% ===============================')

salario = float(input('Insira o salario: R$ '))
novo = salario + (salario * 15 / 100)
print('O salario Original: R$ {} com acréscimode 15% o salario passou a ser R$ {} '.format(salario,novo))

