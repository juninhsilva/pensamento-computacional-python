arroz=18
feijao=6.75
carne=39.98

alimento=[arroz, feijao, carne]

for i in range(len(alimento)):
    if(alimento[i]<=20):
        print('Pode Comprar')
    else:
        print('Nao pode Comprar')
