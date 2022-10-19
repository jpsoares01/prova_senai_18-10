oper = 0

    
qtdF = 0

func = [0 for i in range(5)]
vHor = [0 for i in range(5)]
hNor = [0 for i in range(5)]
hExt = [0 for i in range(5)]

while oper != 3:
    
    if oper == 0:
        print("SENAI Funcontrol 1.0")
        print("--------")
        oper = int(input('Escolha uma opção: \n [1] Cadastrar horas de funcionário \n [2] Consultar holerite \n [3] Encerrar sistema'))
        
    elif oper == 1:
         qtdF = qtdF +1
         retF = qtdF
         func[retF] = input("Nome do funcionário: ")
         vHor[retF] = float(input("Valor da hora normal: "))
         hNor[retF] = float(input("Quantidade de horas normais: "))
         alt = input("Realizou horas extras? (S ou N): ")
         
         if alt == "S":
             hExt[retF] = float(input("Quantidade de horas extras: "))
             if hExt[retF] >20:
                 hExt[retF] = 20
                 print('\n Horas excedidas! Apenas 20h serão contabilizadas.')
         else:
            hExt[retF] = 0
        
         print('\n Informações registradas com sucesso!')
         oper = int(input('Escolha uma opção: \n [1] Cadastrar horas de funcionário \n [2] Consultar holerite \n [3] Encerrar sistema'))
    
    
    elif oper == 2:
        print("SENAI Funcontrol 1.0")
        print("--------")
        print('Existem', qtdF, "funcionarios registrados")
        
        for cont in range(1,qtdF+1):
            print(cont, '-', func[cont])
        refF = int(input("Insira o código do funcionário para exibir seu holerite: "))
        
        tNor = hNor[refF] * vHor[refF]
        tExt = hExt[refF] * vHor[refF] * 1.5
        tVen = tNor + tExt
        
        # INSS
        
        if tVen > 7087.22:
            tInss = 992.21
            inss = 0.14
        
        else:
            
            if tVen > 3641.04:
                inss = 0.14
                
            else:
                
                if tVen > 2427.36:
                    inss = 0.12
                    
                else:
                
                    if tVen > 1212.01:
                        inss = 0.09
                        
                    else:
                        inss = 0.075
                tInss = inss * tVen
                
        # IRPF
        
        if tVen > 4664.68:
            irfp = 0.275
        else:
            if tVen > 3751.06:
                irfp = 0.225
            else:
                if tVen > 2826.66:
                    irfp = 0.15
                else:
                    if tVen > 1903.99:
                        irfp = 0.075
                    else: 
                        irfp = 0
                        
            tIrpf = irfp * tVen
            
            
            
        print ("------------------------------------------------")
        print (" HOLERITE MENSAL SENAI Funcontrol 1.0 ")
        print ("------------------------------------------------")
        print (" Funcionário: ", func[refF], "(R$", vHor[refF], "\n) ")
        print ("------------------------------------------------")
        print (" Descrição Ref Vencimentos Descontos |")
        print (" Salário base ", hNor[refF], "h ", tNor, " 0.00 |")
        print (" Horas extras ", hExt[refF], "h ", tExt, " 0.00 |")
        print (" INSS ", (inss*100), "% 0.00 ", tInss, " |")
        print (" IRPF ", (irfp*100), "% 0.00 ", tIrpf, " |")
        print ("------------------------------------------------|")
        print (" Totais: ", (tNor+tExt), " ", (tInss+tIrpf), " |")
        print ("------------------------------------------------|")
        print (" Salário líquido: R$", (tNor+tExt-tInss+tIrpf), " |")
        print ("------------------------------------------------/")
        oper = int(input('Escolha uma opção: \n [2] Consultar holerite \n [0] Menu principal'))