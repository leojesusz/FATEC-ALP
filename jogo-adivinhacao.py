j01= int(input("Escolha um número entre 1 e 10: "))

while (j01>10) or (j01<1):
    print ("Número Inválido, digite novamente.")
    j01= int(input("Escolha um número entre 1 e 10: "))


j02=  int
chances = 0

while  j02 != j01:
    j02= int(input("Adivinhe um número entre 1 e 10: "))
    chances += 1
    if(j01 == j02):
        print("Você acertou!")
        print("O número de tentativas foi:", chances)
        