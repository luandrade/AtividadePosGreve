'''3) Escreva um programa que receba dois valores inteiros declarados por base e
expoente, e realize a operação de exponenciação da seguinte forma baseexponente.
a) Exemplo: Base = 2; Expoente = 3 ? 2
3 = 2 x 2 x 2 = 8.'''


base = int(input('informe a base \n'))
expoente = int(input('informe o expoente \n'))
acumulador = 1
for c in range (0,expoente):
  acumulador = base*acumulador
print('resultado =',acumulador)
