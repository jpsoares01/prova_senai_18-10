print("Digite 5 vezes o valor de N")

for x in range(5):
    n = int(input(f"{x+1}º valor "))
    
    if n ==0:
        print(" 0 x 0 = 0")
        
    for y in range(n+1):
        print(y,'x',n,'=',y*n)
    print(' ')