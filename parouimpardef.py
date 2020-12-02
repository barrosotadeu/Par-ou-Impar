import random, sys

def resposta():

    if soma % 2 == 0:
        resultado = 'par'

    else:
        resultado = 'impar'
    print(f"Você escolheu a opção {escolha} e o computador escolheu a opção {escolha_computador}.")
    print(f"O resultado da soma é {soma}. É um número {resultado}. ", end='')
    if escolha == resultado:
        print("Você ganhou!")
    else:
        print("Você perdeu!")

while True:

    escolha = input("Escolha (p)ar, (i)mpar ou (s)air: ")
    if escolha != 'p' and escolha != 'i' and escolha != 's':
        print("Digite uma opção válida!")
        continue

    elif escolha == 's':
        break
        sys.exit()

    else:
        numero = int(input("Informe um número de 1 a 999"))



    computador = random.randint(1, 999)

    soma = numero + computador

    if escolha == 'p':
        escolha_computador = 'ímpar'
        escolha = 'par'

    else:
        escolha_computador = 'par'
        escolha = 'ímpar'


    resposta()

