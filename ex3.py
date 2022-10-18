import math

c = 0
n = 1

while n != 0 :
    n = int(input("Digite um valor (0 para parar a entrada dos dados!): "))
    if c==0 or c==5:
        print("Valor    Valor**2    Valor **3   RaizQuadrada")

    rn = math.sqrt(n)
    print(f"{n}         {n**2}          {n**3}            {rn}")

    c += 1
