import random
continuar = True
continuar = "s"
while continuar == "s":
    ns = random.randint(1,10)

    T = 5
    while( T > 0 ):
        print("Você tem", T, "tentativas")
        T = T - 1
        chute = int(input("Digite um numero entre 0 e 10:"))

        if( ns == chute):
            print("Você acertou.")
            T = 0
        else:
            print("Você errou.")
             
    continuar = input("Deseja continuar? Se Sim, digite (s)")

