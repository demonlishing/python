nota = float (input("digite uma nota entre 0 e 10:"))

while nota < 0 or nota >10:
    print("você errou, deve digitar uma nota entre 0 e 10:")
    nota = float(input("digite uma nova nota:"))


print ("essa nota é valida:", nota) 