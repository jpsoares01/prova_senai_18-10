nt = int(input("Quantos numeros deverão ser lidos: "))

for i in range(nt):
    n = int(input("Digite o valor: "))
    if n == 0:
        print("Valor = 0, Fatorial = 1")
    else:
        aux = n
        fat = n
        while aux != 1:
            fat = fat*(aux-1)
            aux -= 1
        print(f"Valor = {n}, Fatorial = {fat}")