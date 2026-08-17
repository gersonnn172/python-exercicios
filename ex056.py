somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
for id in range(1, 5):
    print('---- {}° PESSOA ----'.format(id))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaidade += idade
    if id == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos de idade, e se chama {}'.format(maioridadehomem, nomevelho))