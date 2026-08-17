valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento: '))
prestação = valor / (anos * 12)
print('Para pagar uma casa de {:.2f} em {:.1f} anos'.format(valor, anos), end='')
print(' a prestação será de R${:.2f} '.format(prestação))
if prestação >  (salario * 30 / 100):
    print('Emprestimo NEGADO')
else:
    print('Emprestimo CONCEDIDO!!')
