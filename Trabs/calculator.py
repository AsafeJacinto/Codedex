Q1 = int(input('Qual área você gostaria de calcular? \n 1 - Quadrado \n 2 - Retângulo \n 3 - Triângulo \n 4 - Círculo \n'))

if Q1 == 1:

    lado = int(input('Digite o valor do lado do quadrado: '))
    area = lado ** 2
    print(f'A área do quadrado é: {area}')


elif Q1 == 2:
    
    altura = int(input('Digite o valor da altura: '))
    base = int(input('Digite o valor da base: '))
    area = altura * base 
    print (f'A área do retangulo é: {area}')


elif Q1 == 3:

    altura = int(input('Digite o valor da altura: '))
    base = int(input('Digite o valor da base: '))
    area = (altura * base)/2
    print (f'A area do triangulo é: {area}')


elif Q1 == 4:
    raio = int(input('Digite o valor do raio: '))
    area = 3.14 * raio ** 2
    print (f'A area do circulo é: {area}')

    
else:
    print('Digite uma opção válida')
