print("Digite 10 valores!")
di = 0
fi = 0
for i in range(10):
    v = int(input("Valor: "))

    if v >= 10 and v <=20:
        di += 1

    else:
        fi += 1

print("Dos 10 valores digitados")
print(f"{di} estão dentro so intervalo de 10 e 20")
print(f"e {fi} não estão nesse intervalo!")
