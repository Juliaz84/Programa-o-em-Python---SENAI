

# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.

n1 = int(input('Insira um numero: '))

if n1 >= 0:
    print('Positivo')
else:
    print('Negativo')


# 2*

# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.

idade = int(input('Digite sua idade: '))

if idade >= 16:
    print('Pode votar')
else:
    print('Não pode votar')



# 3*

# Declara uma variável com um número qualquer, 
# determine se um número é par ou ímpar.

var = 2

if var % 2 == 0:
    print('Ele é par')
else:
    print('Ele é impar')


# 4*

# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno
# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.


t1 = float(input('Digite um numero: '))
t2 = float(input('Digite um numero: '))
t3 = float(input('Digite um numero: '))

if t1 == t2 == t3 == t1 :
    print('Equilatero')
elif t1 != t2 != t3 != t1:
    print('Isosceles')
else: 
    print('Escaleno')

# 5*

# Determine se um número é múltiplo de 5 e 7.

n = int(input('Insira um numero: '))

if n % 5== 0 and n % 7== 0:
    print('Multiplo de 5 e 7')
else:
    print('Não é multiplo')

# 6*

# Verifique se um número é positivo e maior que 10

n2 = int(input('Numero: '))

if n2 >= 0 and n2 > 10:
    print('Correto')
else:
    print('Errado')

# 7*

# Verifique se um número é divisível por 3 ou 5.

n2 = int(input('Numero: '))

if n2 / 3 == 0 or n2 / 5 ==0:
    print('Correto')
else:
    print('Errado')