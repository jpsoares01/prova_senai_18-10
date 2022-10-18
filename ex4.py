print("Dada a equação E=1+1/1!+1/2!+1/3!+1/N!")

n = int(input("Digite um valor inteiro e positivo para N: "))

while n < 0:
    n = int(input("Erro! Digite um valor positivo!: "))

if n == 0:
    aux = 1
else:
    aux = n
    while n != 1:
        aux = aux*(n-1)
        n -= 1

print("E=",1+1/(1*1)+1/(2*1)+1/(3*2*1)+1/aux)
