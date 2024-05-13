import random
 
continuar = "S"
pERRO = 0
pCERTO = 0

while continuar.upper() == "S":
    ns = random.randint(1,10)
    T = 3
    while(T > 0):
        print("Você tem", T, " Tentativas")
        T = T - 1
        nc = int(input("Digite um número entre 1 e 10:"))
        if (ns == nc):
            print("Você acertou.")
            T = 0
            pCERTO = pCERTO + 1
        else:
            print("Você errou.")
            pERRO = pERRO + 1
        print("Número de acertos:", pCERTO)
        print("Número de errros:", pERRO)



    continuar = input("Deseja continuar? (S)im:")
