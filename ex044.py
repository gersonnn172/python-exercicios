compras = float(input('Preço das Compras: R$ '))
print('FORMAS DE PAGAMENTOS')
op1 = compras - (compras * 10 / 100)
print('[ 1 ] à vista dinheiro')
op2 = compras - (compras * 5 / 100)
print('[ 2 ] à vista cartão')
op3 = (compras + (compras * 5 / 100)) / 6
print('[ 3 ] 2x no cartão')
op4 = (compras + (compras * 10 / 100)) / 3
print('[ 4 ] 3x ou mais no cartão')
opção = int(input('Qual é a opção? '))
if opção == 1:
    print('Sua compra á vista no dinheiro será {:.2f} e terá desconto de 10%'.format(compras))
    print('Sua compra com desconto vai de {:.2f} para {:.2f}'.format(compras, op1))
elif opção == 2:
    print('Sua compra à vista no cartão será {:.2f} e terá desconto de 5%'.format(compras))
    print('Sua compra no cartão a vista vai de {:.2f} para {:.2f}'.format(compras, op2))
elif opção == 3:
    print('Sua compra no cartão parcelado em 2x ficaria {:.2f} mais tem juros de 5%'.format(compras))
    print('Com o juros a sua compra que seria de {:.2f}, passa a ser {:.2f}'.format(compras, op3))
elif opção == 4:
    print('Sua compra no cartão parcelado em 3x ficaria {:.2f}, mais tem juros de 10%'.format(compras))
    print('Com o juros a sua compra que seria de {:.2f}, passa a ser {:.2f}'.format(compras, op4))
else:
    print('Opção invalida, tente as alternativas de 1 a 4.')