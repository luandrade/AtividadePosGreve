'''2) Escreva um algoritmo que calcule o fatorial de um número inteiro lido. Considere que
para calcular o fatorial de um número N a seguinte operação é obedecida:
N! = 1 x 2 x 3 x ... x N-1 x N, portanto 3! = 1 x 2 x 3 = 6; e
0! = 1.'''

NumeroFat = eval(input(" Digite o número a ser fatorado: "))
fatorial = 1


if(NumeroFat != 0):
  for i in range(1, NumeroFat+1):
    fatorial = fatorial * i
  
else:
  print('O fatorial de 0 é 1')
  
print('fatorial de',NumeroFat,'é =',fatorial)
