print('\n Olá seja bem vindo ao labirinto da floresta')
name = input('Para começarmos me diga seu nome: ')
print (f'\n {name} isso? que nome bonito')
item = int(input('Agora antes de sairmos explorar, me diga que item você levará: \n ' \
'\n 1 - Corda' \
'\n 2 - Faca' \
'\n 3 - Kit de primeiro soccoro' \
'\n 4 - Capa da Chapeuzinho Vermelho' \
'\n \n  Então o que acha que será útil?  '))
print('\n \n ======================================')
print ('\n \n Perfeito, então vamos entrar no nosso helicoptero e vamos lá')

vivo = True

#retorno ao inicio do labirinto
while vivo:
    if not vivo:
        break
    #entrada no labirinto
    entrada = int(input('Chegamos você dejesa entrar?\n' \
    '\n 1 - Obvio eu vim para isso sou um aventureiro desde que nasci' \
    '\n 2 - Não... sou medroso e prefiro ficar em casa jogando no celular \n '))
    #entrou no labirinto
    if entrada == 1:
        print ('\n \n ======================================')
        print('\n Perfeito  vamos lá' )
        print('\n Você entra por um portico de pedra todo cheio de musgos' \
        '\n e logo se depara com uma bifurcação o caminho da direita está cheio de vinhas' \
        '\n o da esquerda está livre e com uma leve brisa vindo dele')
        
        #retorno a primeira escolha de lados
        while True:
            if not vivo:
                break
            
            b1 = int(input('Qual lado você seguira?' \
            '\n 1 - Lado direito' \
            '\n 2 - Lado esquerdo \n'))
        #b1 lado direito
            if b1 == 1 and item != 2:
                print ('\n \n ======================================')
                print (f'\n Você  não possui a Faca, lembra disso?')
                continue

            elif  b1 == 1 and item == 2:
                print ('\n \n ======================================')
                print ('\n Você vai cortando as vinhas com sua Faca,' \
                '\n você percebe que elas continuam em frente mas há buraco na parede a sua esquerda,' \
                '\n ele é estreito mas você passa por ele.')
            #buraco do caminho das cobras    
                b12 = int(input ('\n o que fará?'\
                '\n 1 - Seguir reto cortando as vinhas' \
                '\n 2 - Entrar pelo buraco na parede' \
                '\n 3 - Voltar '))
            #morte pelas cobras        
                if b12 == 1:
                    print ('\n \n ======================================')
                    print ('\n Você segue cortando até que percebe que as vinhas à sua frente na verdade'
                    '\n UM NINHO DE COBRAS, você tenta correr mas uma cobra já havia se enrolado em sua perna')
                    cobra = int(input('O que você fara?'
                    '\n 1 - Começa a se debater e tenta fugir'
                    '\n 2 - Aceita a morte iminente '))

                    if cobra == 1:
                        print ('\n \n ======================================')
                        print ('\n Você consegue se soltar e voltar correndo, mas o veneno está em suas veias'
                        '\n Você MOREE')
                        vivo = False
                        break
                    else:
                        print ('\n \n ======================================')
                        print ('\n Você MORRE')
                        vivo = False
                        break


            #entra no buraco
                elif b12 == 2:
                    print ('\n \n ======================================')
                    print ('\n Você passa por aquele buraco apertado' \
                    '\n ao passar sente um forte vento que quase derruba você' \
                    '\n você olha em direção ao vento e vê um buraco que deveria ter uns 3 a 4 metros de largura,' \
                    '\n provavelmente o chão que quebrou.' \
                    '\n\n Você segue pela direita do buraco, unico caminho que resta.' \
                    '\n chega numa curva que se separa em dois caminhos.' \
                    '\n 1 - Uma ladeira' \
                    '\n 2 - Uma escadaria')
                    escada = int(input('Qual você escolhe? '))
                    #Escadaria ou Ladeira
                    if escada == 1:
                        print ('\n \n ======================================')
                        print ('\n Você começa a subir, é meio escorregadio mas está conseguindo subir,' \
                        '\n você da uma pausa para descansar e escora a mão na parede...' \
                        '\n sem querer aciona uma armadilha, e uma pedra gigante começa a rolar ladeira a baixo' \
                        '\n você tenta correr.... mas é pego' \
                        '\n Você MORRE')
                        vivo = False
                        break
                        
                
                    else:
                        print ('\n \n ======================================')
                        print ('\n Você começa a subir a escadaria...' \
                        '\n é longa mas você treinou os gluteos na academia e segue firme.' \
                        '\n você começa a ver o fim da escadaria' \
                        '\n quando chega começa ver um clarão no final do corredor' \
                        '\n ao entrar na sala se depara com outros corredores que se encontraram na mesma sala,' \
                        '\n uma esmeralda EXATAMENTE igual a do Minecraft.' \
                        '\n PARABÉNS VOCÊ GANHOU DO LABIRINTO')
                        vivo = False
                        break        
            #volta pro inicio    
                else:
                    continue


        #b1 Lado Esquerdo    
            if b1 == 2:
                print ('\n \n ======================================')
                print ('\n Você vai caminhando e o vento vai se intensificando,' \
                '\n você se depara com uma parede bem alta com um lançador de corda no chão,' \
                '\n percebe que consegue utiliza-lo'\
                '\n 1 - usar o lançador de corda até o alto da parede' \
                '\n 2- seguir caminho')
                lanCorda = int(input('O que você faz? '))

            while True:
                if not vivo:
                    break

                #if lancador de corda
                if lanCorda == 1 and item == 1:
                    print ('\n \n ======================================')
                    print ('\n Você coloca sua corda nele e atira até o topo' \
                    '\n você se agarra bem firme na corda e começa a subir' \
                    '\n você sobe por um tempo e pensa que altura você já esta...' \
                    '\n 1 - Focar na subida' \
                    '\n 2 - Olhar para baixo')
                    olhar = int(input('O que você faz? '))
                        
                        #if olha pra baixo
                    if olhar == 1:
                        print ('\n \n ======================================')
                        print ('\n quando chega começa ver um clarão no final do corredor' \
                        '\n ao entrar na sala se depara com outros corredores que se encontraram na mesma sala,' \
                        '\n uma esmeralda EXATAMENTE igual a do Minecraft.' \
                        '\n PARABÉNS VOCÊ GANHOU DO LABIRINTO')                    
                        vivo = False
                        break
                        
                    else:
                        print ('\n \n ======================================')
                        print ('\n Você olha para baixo e se apavora com a altura,' \
                        '\n começa a se subir se tremendo de medo,' \
                        '\n acaba acelerando a subida e sem querer....' \
                        '\n escorrega a mão e acaba caindo tudo.' \
                        '\n você MORRE')
                        vivo = False
                        break
                else:
                    print ('\n \n ======================================')
                    print ('\n Você lembra que não trouxe a corda e segue caminho' \
                    '\n percebe que o vento vai ficando mais forte' \
                    '\n ao longe você ve ums estrutura como um ventilador gigante' \
                    '\n e ao olhar vê uma fenda de uns 3/4 metros' \
                    '\n e a continuação do labirinto logo após a fenda' \
                    '\n e a parede do lado há uma corda amarrada de uma ponta à outra' \
                    '\n 1 - Virar o ventilador para o buracao e voar até o outro lado' \
                    '\n 2 - Se segurar na corda para atravessar')
                    vent = int(input('O que você faz? '))

                    #ventilador
                    if vent == 1 and item != 4:
                        print ('\n \n ======================================')
                        print ('\n Você vira o ventilador e se prepara para voar,' \
                        '\n ao pular você percebe que o vento não é forte o suficiente' \
                        '\n você cai no buraco e MORRE')
                        vivo = False
                        break

                    elif vent == 1 and item == 4:
                        print('\n \n ======================================')
                        print('\n Você vira o ventilador e se prepara para voar' \
                        '\n antes de pular você lembra que trouxe' \
                        '\n A CAPA DA CHÁPEUZINHO VERMELHO e decide vestir ela.' \
                        '\n Você pula e o vento bate na capa o fazendo planar até o outro lado' \
                        '\n você chega do outro lado inteiro' \
                        '\n você segue camino e vê um buraco na parede a sua direita e decide entrar' \
                        '\n mas percebe que está cheio de vinhas e não consegue ir para o outro lado,' \
                        '\n volta e segue caminho' \
                        '\n chega numa curva que se separa em dois caminhos.' \
                        '\n 1 - Uma ladeira' \
                        '\n 2 - Uma escadaria')
                        escada = int(input('Qual você escolhe? '))
                        #Escadaria ou Ladeira
                        if escada == 1:
                            print ('\n \n ======================================')
                            print ('\n Você começa a subir, é meio escorregadio mas está conseguindo subir,' \
                            '\n você da uma pausa para descansar e escora a mão na parede...' \
                            '\n sem querer aciona uma armadilha, e uma pedra gigante começa a rolar ladeira a baixo' \
                            '\n você tenta correr.... mas é pego' \
                            '\n Você MORRE')
                            vivo = False
                            break
                    
                        else:
                            print ('\n \n ======================================')
                            print ('\n Você começa a subir a escadaria...' \
                            '\n é longa mas você treinou os gluteos na academia e segue firme.' \
                            '\n você começa a ver o fim da escadaria' \
                            '\n quando chega começa ver um clarão no final do corredor' \
                            '\n ao entrar na sala se depara com outros corredores que se encontraram na mesma sala,' \
                            '\n uma esmeralda EXATAMENTE igual a do Minecraft.' \
                            '\n PARABÉNS VOCÊ GANHOU DO LABIRINTO')
                            vivo = False
                            break
                        
                    else:
                        print ('\n \n ======================================')
                        print ('\n Você se agarra firme na corda e vai' \
                        '\n sente a corda balançar mas segue firme' \
                        '\n quase no final a corda arrebenda fazendo você bater com tudo na quina' \
                        '\n você se corta e começa a sangrar' \
                        '\n começa a pensar numa solução' \
                        '\n 1 - usar um kit medico' \
                        '\n 2 - rasgar um pedaço da camisa para tentar estancar o sangue')
                        corte = int(input('O que você faz? '))

                        #if do kit medico
                        if corte == 1 and item == 3:
                            print ('\n \n ======================================')
                            print ('\n Você usa o Kit médico e consegue parar o sangramento' \
                            '\n você segue camino e vê um buraco na parede a sua direita e decide entrar' \
                            '\n mas percebe que está cheio de vinhas e não consegue ir para o outro lado,' \
                            '\n volta e segue caminho' \
                            '\n chega numa curva que se separa em dois caminhos.' \
                            '\n 1 - Uma ladeira' \
                            '\n 2 - Uma escadaria')
                            escada = int(input('Qual você escolhe? '))
                            #Escadaria ou Ladeira
                            if escada == 1:
                                print ('\n \n ======================================')
                                print ('\n Você começa a subir, é meio escorregadio mas está conseguindo subir,' \
                                '\n você da uma pausa para descansar e escora a mão na parede...' \
                                '\n sem querer aciona uma armadilha, e uma pedra gigante começa a rolar ladeira a baixo' \
                                '\n você tenta correr.... mas é pego' \
                                '\n Você MORRE')
                                vivo = False
                                break
                        
                            else:
                                print ('\n \n ======================================')
                                print ('\n Você começa a subir a escadaria...' \
                                '\n é longa mas você treinou os gluteos na academia e segue firme.' \
                                '\n você começa a ver o fim da escadaria' \
                                '\n quando chega começa ver um clarão no final do corredor' \
                                '\n ao entrar na sala se depara com outros corredores que se encontraram na mesma sala,' \
                                '\n uma esmeralda EXATAMENTE igual a do Minecraft.' \
                                '\n PARABÉNS VOCÊ GANHOU DO LABIRINTO')
                                vivo = False
                                break
                            
                        elif corte == 1 and item !=3:
                            print ('\n \n ======================================')
                            print ('\n Você começa a revirar sua mochila procurando o Kit Médico,' \
                            '\nAté lembrar que você não trouxe ele, nessa demora você perde muito sangue e desmaia...' \
                            '\n VOCÊ MORRE')
                            vivo = False
                            break

                        else:
                            print ('\n \n ======================================')
                            print('\n Você rapidamente rasga sua camisa e amarra com todas as forças, ' \
                            '\n não fica perfeito mas funciona' \
                            '\n você segue camino e vê um buraco na parede a sua direita e decide entrar' \
                            '\n mas percebe que está cheio de vinhas e não consegue ir para o outro lado,' \
                            '\n volta e segue caminho' \
                            '\n chega numa curva que se separa em dois caminhos.' \
                            '\n 1 - Uma ladeira' \
                            '\n 2 - Uma escadaria')
                            escada = int(input('Qual você escolhe? '))
                            #Escadaria ou Ladeira
                            if escada == 1:
                                print ('\n \n ======================================')
                                print ('\n Você começa a subir, é meio escorregadio mas está conseguindo subir,' \
                                '\n você da uma pausa para descansar e escora a mão na parede...' \
                                '\n sem querer aciona uma armadilha, e uma pedra gigante começa a rolar ladeira a baixo' \
                                '\n você tenta correr mas sua ferida o impede de ser rapido o suficiente.... mas é pego' \
                                '\n Você MORRE')
                                vivo = False
                                break
                        
                            else:
                                print ('\n \n ======================================')
                                print ('\n Você começa a subir a escadaria...' \
                                '\n é longa mas você treinou os gluteos na academia e segue firme.' \
                                '\n você começa a ver o fim da escadaria' \
                                '\n quando chega começa ver um clarão no final do corredor' \
                                '\n ao entrar na sala se depara com outros corredores que se encontraram na mesma sala,' \
                                '\n uma esmeralda EXATAMENTE igual a do Minecraft.' \
                                '\n PARABÉNS VOCÊ GANHOU DO LABIRINTO')
                                vivo = False
                                break
                        

    else:
        print ('\n \n ======================================')
        print(f'eh... vamor para casa {name} prefere se aventurar em simuladores')
        recomeço = int(input('\n \n  Então vai mudar de ideia?\n '
        '\n 1 - Sim vamos lá!!'
        '\n 2 - Não \n ')) 
        if recomeço == 1:
            continue
        else:
            print('\n \n ======================================')
            break

print ('Obrigado por jogar')        
print('\n \n ======================================')
