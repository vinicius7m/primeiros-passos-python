print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 43

chute_str = input("Digite seu número:  ")
chute = int(chute_str)

print("Voce digitou ", chute)
print(type(chute))

acertou = chute == numero_secreto
maior   = chute > numero_secreto
menor   = chute < numero_secreto

if (acertou):
    print("*************")
    print("Você acertou!")
    print("*************")
else:
    if(maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif(menor):
        print("Você errou! O seu chute foi menor que o número secreto.")

print("Fim do jogo!")