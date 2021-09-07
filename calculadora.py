from time import sleep
from emoji import emojize
n1 = int(input("Informe o 1º numero: "))
n2 = int(input("Informe o 2º numero: "))
print("Qual das operações você deseja escolher?")
opcao = int(input("""
[1] - SOMAR
[2] - MULTIPLICAR
[3] - SUBTRAÇÃO
[4] - DIVISÃO
[5] - MAIOR
[6] - NOVOS NUMEROS
[7] - SAIR DO PROGRAMA
OPÇÃO: """))
while opcao > 8 or opcao < 0:
    print("Essa opção não existe!!")
    opcao = int(input("""
[1] - SOMAR
[2] - MULTIPLICAR
[3] - SUBTRAÇÃO
[4] - DIVISÃO
[5] - MAIOR
[6] - NOVOS NUMEROS
[7] - SAIR DO PROGRAMA
OPÇÃO: """))
else:
    if opcao == 1:
        soma = n1 + n2
        print("A soma dos dois numeros será: {}".format(soma))
    elif opcao == 2:
        mult = n1*n2
        print("A multiplicação desses dos dois numeros será: {}".format(mult))
    elif opcao == 3:
        sub = n1 - n2
        print("A subtração desses dois numeros será: {}".format(sub))
    elif opcao == 4:
        div = n1 / n2
        print("A divisao desses dois numeros será: {}".format(div))
    elif opcao == 5:
        while n1 == n2:
            print("Os numeros são iguais")
            n1 = int(input("Informe o 1º numero: "))
            n2 = int(input("Informe o 2º numero: "))
        if n1 > n2:
            print("O valor de N1({}) é maior que o N2({})".format(n1,n2))
        else:
            print("O valor de N2({}) é maior que o N1({})".format(n2,n1))
    elif opcao == 6:
        while opcao == 6:
            n1 = int(input("Informe o 1º numero: "))
            n2 = int(input("Informe o 2º numero: "))
            opcao = int(input("Opção: "))
        else:
            if opcao == 1:
                soma = n1 + n2
                print("A soma dos dois numeros será: {}".format(soma)) 
            elif opcao == 2:
                mult = n1*n2
                print("A multiplicação desses dos dois numeros será: {}".format(mult))
            elif opcao == 3:
                sub = n1 - n2
                print("A subtração desses dois numeros será: {}".format(sub))
            elif opcao == 4:
                div = n1 / n2
                print("A divisao desses dois numeros será: {}".format(div))
            elif opcao == 5:
                while n1 == n2:
                    print("Os numeros são iguais")
                    n1 = int(input("Informe o 1º numero: "))
                    n2 = int(input("Informe o 2º numero: "))
                if n1 > n2:
                    print("O valor de N1({}) é maior que o N2({})".format(n1,n2))
                else:
                    print("O valor de N2({}) é maior que o N1({})".format(n2,n1))
            else:
                print("Até mais ,jovem padawan")
                breakpoint       
    else:
        print("finalizando...")
        sleep(1)
        print(emojize("Até mais ,jovem padawan :sunglasses:",use_aliases=True))
        breakpoint