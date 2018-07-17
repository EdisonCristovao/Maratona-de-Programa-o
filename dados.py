
comb = []

def jogarDado(n):
    if n == 0:
        return 0

    for x in range(1,7):
        comb.append(x)
    imprimir()
    jogarDado(n-1)
        
def imprimir():
    for x in range(1,7):
        print(comb[x-1]),

jogarDado(2)
        

