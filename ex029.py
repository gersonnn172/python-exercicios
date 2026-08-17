velocidade = float(input('Qual a velocidade do seu carro?'))
if velocidade > 80:
    print('MULTADO!!!, Voce excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade - 80) * 7
    print('Voce deverá pagar R${:.2f} de multa'.format(multa))
else:
    print('Tenha um bom dia! dirija com cuidado')
