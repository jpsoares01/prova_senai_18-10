b = 0
cont = 0


while cont < 5:
    a = int(input("Digite o valor parA 'a': "))
    if a < 0:
        b += 1
    cont += 1
    
    
if b == 1:
    print(f"Dos 5 valores para a, {b} é negativo!")

else:
    print(f"Dos 5 valores para a, {b} são negativos!")