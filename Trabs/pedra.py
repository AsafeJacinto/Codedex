import random

player = int(input('Bem vindo ao Pedra, Papel, Tesoura, Lagarto e Spock ' \
'\n Para começar escolha uma das opções: ' \
'\n 1 - Pedra ✊' \
'\n 2 - Papel ✋' \
'\n 3 - Tesoura ✌️' \
'\n 4 - Lagarto 🦎' \
'\n 5 - Spock 🖖 \n' ))

cpu = random.randint(1,5)



if player == 1 and cpu == 2:
    print (f'Você: {player} - Pedra ✊ \n CPU: {cpu} - Papel ✋ \n Resultado: Você Perdeu')
elif player == 1 and cpu == 3:
    print (f'Você: {player} - Pedra ✊ \n CPU: {cpu} - Tesoura ✌️ \n Resultado: Você Ganhou')
elif player == 1 and cpu == 4:
    print (f'Você: {player} - Pedra ✊ \n CPU: {cpu} - Lagarto 🦎 \n Resultado: Você Ganhou')   
elif player == 1 and cpu == 5:
    print (f'Você: {player} - Pedra ✊ \n CPU: {cpu} - Spock 🖖 \n Resultado: Você Perdeu')
elif player == 1 and cpu == 1:
    print (f'Você: {player} - Pedra ✊ \n CPU: {cpu} - Pedra ✊ \n Resultado: Empate')


elif player == 2 and cpu == 1:
    print (f'Você: {player} - Papel ✋ \n CPU: {cpu} - Pedra ✊ \n Resultado: Você Ganhou')
elif player == 2 and cpu == 3:
    print (f'Você: {player} - Papel ✋ \n CPU: {cpu} - Tesoura ✌️ \n Resultado: Você Perdeu')
elif player == 2 and cpu == 4:
    print (f'Você: {player} - Papel ✋ \n CPU: {cpu} - Lagarto 🦎 \n Resultado: Você Perdeu')
elif player == 2 and cpu == 5:
    print (f'Você: {player} - Papel ✋ \n CPU: {cpu} - Spock 🖖 \n Resultado: Você Ganhou')
elif player == 2 and cpu == 2:
    print (f'Você: {player} - Papel ✋ \n CPU: {cpu} - Papel ✋ \n Resultado: Empate')

elif player == 3 and cpu == 1:
    print (f'Você: {player} - Tesoura ✌️ - Pedra ✊ \n Resultado: Você Perdeu')
elif player == 3 and cpu == 2:
    print (f'Você: {player} - Tesoura ✌️ \n CPU: {cpu} - Papel ✋ \n Resultado: Você Ganhou')
elif player == 3 and cpu == 4:
    print (f'Você: {player} - Tesoura ✌️ \n CPU: {cpu} - Lagarto 🦎 \n Resultado: Você Ganhou')
elif player == 3 and cpu == 5:
    print (f'Você: {player} - Tesoura ✌️ \n CPU: {cpu} - Spock 🖖 \n Resultado: Você Perdeu')
elif player == 3 and cpu == 3:
    print (f'Você: {player} - Tesoura ✌️ \n CPU: {cpu} - Tesoura ✌️ \n Resultado: Empate')

elif player == 4 and cpu == 1:
    print (f'Você: {player} - Lagarto 🦎 \n CPU: {cpu} - Pedra ✊ \n Resultado: Você Perdeu')
elif player == 4 and cpu == 2:
    print (f'Você: {player} - Lagarto 🦎 \n CPU: {cpu} - Papel ✋ \n Resultado: Você Ganhou')
elif player == 4 and cpu == 3:
    print (f'Você: {player} - Lagarto 🦎 \n CPU: {cpu} - Tesoura ✌️ \n Resultado: Você Perdeu')
elif player == 4 and cpu == 5:
    print (f'Você: {player} - Lagarto 🦎 \n CPU: {cpu} - Spock 🖖 \n Resultado: Você Ganhou')
elif player == 4 and cpu == 4:
    print (f'Você: {player} - Lagarto 🦎 \n CPU: {cpu} - Lagarto 🦎 \n Resultado: Empate')

elif player == 5 and cpu == 1:
    print (f'Você: {player} - Spock 🖖 \n CPU: {cpu} - Pedra ✊ \n Resultado: Você Ganhou')
elif player == 5 and cpu == 2:
    print (f'Você: {player} - Spock 🖖 \n CPU: {cpu} - Papel ✋ \n Resultado: Você Perdeu')
elif player == 5 and cpu == 3:
    print (f'Você: {player} - Spock 🖖 \n CPU: {cpu} - Tesoura ✌️ \n Resultado: Você Ganhou')
elif player == 5 and cpu == 4:
    print (f'Você: {player} - Spock 🖖 \n CPU: {cpu} - Lagarto 🦎 \n Resultado: Você Perdeu')
elif player == 5 and cpu == 5:
    print (f'Você: {player} - Spock 🖖 \n CPU: {cpu} - Spock 🖖 \n Resultado: Empate')

else:
    print('Escolha uma opção válida')