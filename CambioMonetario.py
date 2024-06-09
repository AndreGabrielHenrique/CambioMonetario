separador="-"*90
print(f"{separador}\nConversor de moedas\n{separador}")
moeda=input("Qual a moeda a ser convertida?")
while not moeda:
    print("Campo em branco, favor reinserir.")
    moeda=input("Qual a moeda a ser convertida?")
valormoeda=input("Digite o valor")
while not valormoeda or valormoeda.isalpha():
    print("Campo em branco ou com caracteres, favor reinserir.")
    valormoeda=input("Digite o valor")
conversaomoeda=input("Qual a moeda usada para converter?")
while not conversaomoeda:
    print("Campo em branco, favor reinserir.")
    conversaomoeda=input("Qual a moeda usada para converter?")
valorconversaomoeda=input("Digite o valor")
while not valorconversaomoeda or valorconversaomoeda.isalpha():
    print("Campo em branco ou com caracteres, favor reinserir.")
    valorconversaomoeda=input("Digite o valor")
valorconvertido=float(valormoeda)*float(valorconversaomoeda)
valorconvertidoarredondado=round(valorconvertido,2)
print(f"{separador}\n{valormoeda.replace('.',',')} {moeda} convertido no câmbio de {conversaomoeda} no valor de {valorconversaomoeda.replace('.',',')} fica {str(valorconvertidoarredondado).replace('.',',')} {moeda}.\n{separador}")