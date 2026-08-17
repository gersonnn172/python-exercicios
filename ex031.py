distancia = float(input('Qual a distancia da sua viagem: '))
print('Voce esta prestes a começar uma viagem de {}Km'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('O preço da sua passagem é R${:.2f}'.format(preço))

