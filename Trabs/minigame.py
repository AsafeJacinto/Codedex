print('\n Olá seja bem vindo ao labirinto da floresta')
name = input('Para começarmos me diga seu nome: ')
print (f'\n {name} isso? que nome bonito')
item = int(input('Agora antes de sairmos explorar, me diga que item você levará: \n ' \
'\n 1 - Corda' \
'\n 2 - Faca' \
'\n 3 - Kit de primeiro soccoro' \
'\n 4 - Capa da Chapeuzinho Vermelho' \
'\n \n  Então o que acha que será útil?  '))
print ('\n \n Perfeito, então vamos entrar no nosso helicoptero e vamos lá')

print ('\n \n ====================================== \n \n ')

entrada = int(input('Chegamos você dejesa entrar?\n' \
'\n 1 - Obvio eu vim para isso sou um aventureiro desde que nasci' \
'\n 2 - Não... sou medroso e prefiro ficar em casa jogando no celular \n '))

if entrada == 1:
    print('\n perfeito  vamos lá' )
else:
    print ('\n \n ======================================')
    print(f'eh... vamor para casa o {name} prefere se aventurar em simuladores')
    recomeço = int(input('\n \n  Então vai mudar de ideia?\n '
    '\n 1 - Sim vamos lá!!'
    '\n 2 - Não \n '))