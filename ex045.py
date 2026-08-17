from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
print('-=' * 12)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 12)
if computador == 0:
    if jogador == 0:
       print('EMPATE!')
    elif jogador == 1:
        print('VOCE VENCEU!!')
    elif jogador == 2:
        print('VOCE PERDEU')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('VOCE PERDEU')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('VOCE VENCEU!!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('VOCE VENCEU!!')
    elif jogador == 1:
        print('VOCE PERDEU')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
else:
    print('JOGADA INVÁLIDA')
