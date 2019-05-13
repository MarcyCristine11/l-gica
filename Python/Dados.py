# Meu primeiro programa!

from random import randint  # Importa a função de gerar números aleatórios<3

print("Jodo de Dados")

dado1 = randint(1, 6)  # Gera um número entre 1 e 6 aleatoriamente<3
print("Dado 1: ", dado1)

dado2 = randint(1, 6) # Nome da variável não pode por espaço, se não não funciona!
print("Dado 2: ", dado2)

dado3 = randint(1, 6) # Nome da variável não pode por letra maiúscula, se não não funciona!
print("Dado 3: ", dado3)

dado4 = randint(1, 6)
print("Dado 4: ", dado4)

jogador1 = dado1 + dado2 # Soma as variáveis<3
jogador2 = dado3 + dado4

print('Jogador 1: ', jogador1) 
print('Jogador 2: ', jogador2) 

if jogador1 > jogador2: # Se jogador1 for maior que jogador2:
    print("Jogador 1 venceu!")
else:
    if jogador2 > jogador1:
        print("Jogador 2 venceu!")
    else:
        print("Empate!") 