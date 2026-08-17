num = int(input("Digite seu numero para saber qual a tabuada dele: "))
for c in range(1, 11):
    print("{} x {:2} = {}".format(num , c, num*c))