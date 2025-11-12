import random
import time


def num():
    return random.randint(5,10)
    

def num2():
    return random.randint(5,10), random.randint(5,10), random.randint(5,10)
    

def num3():
    return random.randrange(10,30,1)


def num4():

    for n in range(10,0,-1):
        print(n)
        time.sleep(1)
    print('FOGO')

def num5():

    a = int(input('Insira um numero positivo: '))
    soma = 0  

    for n in range(1, a):
    
     if n % 2 == 0:
        soma += n 
        print(f'A soma: {soma}')

def num6():

    a = int(input('Insira um numero inteiro: '))

    for n in range(1,11):

        mult = a * n
        print(f'{mult}')

def num7():
    for n in range(100,0,-1):
        if n % 2 == 1:
            print(n)
