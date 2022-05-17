from pickletools import OpcodeInfo

def conversor (valor_dolar):
    bolivares = input ("Cuantos Bs tienes ?: ")
    bolivares = float (bolivares)
    dolares = bolivares / valor_dolar
    dolares = round (dolares,2)
    dolares = str (dolares)
    print(" Tienes $ "  + dolares +  " dolares ") 



menu = """ Bienvenidos a tu conversor de bs a dolares 
1 - Bs a la tasa en Paralelo
2 - Bs a la tasa de BCV
3 - Bs con la tasa de Binance 
 Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    conversor (4.45) 
elif opcion == 2:
    conversor (4.33)
elif opcion == 3:
    conversor(4.31)
 
else:
    print( " Por favor elige una opcion correcta")





