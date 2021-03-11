loop = True
lista = []

while(loop):
    numero = int(input("Digite numero a quantidade que quiser, ou zero para encerrar\n"))
    if numero != 0:
        lista.append(numero)
    
    else:
        loop = False

print ("A quantidade de valores inseridos é de", len(lista))

