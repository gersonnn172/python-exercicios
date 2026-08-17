r1 = int(input('Primeiro segmento: '))
r2 = int(input('Segundo segmento: '))
r3 =int(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r1:
    print('Os segmentos acima podem formar um triâgulo!', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
            print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
        print('Os segmentos acima NÃO PODEM formar um triângulo')
