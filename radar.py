velocidade = float(input("Qual a velocidade Atual do carro em km/h-->"))

def result(velocidade):
    if velocidade > 80:
        print("MULTADO")
        print("MULTADO,Por execeder o limite permitido de 80km/h")
        multa = 90 +((velocidade - 80)*5)
        print("o Valor da multa é de R${:.2f}!".format(multa) )
    else:
        print("Voce esta dentro do limite de Velocidade \n Tenha um Bom Dia \nDirigia com segurança")
    return
x = result(velocidade)    