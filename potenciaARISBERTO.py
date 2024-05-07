B = int(input("Digite um número para a base da potencia:"))
E = int(input("Digite um número para o expoente da potencia:"))
R = B

for g in range(1, E):
    R= R * B
print("Resultado:", "{:.2f}".format(R))
