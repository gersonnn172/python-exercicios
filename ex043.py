peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
IMC = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(IMC))
if IMC < 18.5:
    print('Abaixo do Peso!')
elif 18.5 <= IMC < 25:
    print('Peso ideal!!!')
elif  25 <= IMC < 30:
    print('Sobrepeso!')
elif  30 <= IMC < 40:
    print('Obesidade!')
else:
    print('Obesidade Mórbida')

