'''4) Faça um algoritmo que leia um número N, some todos os números inteiros de 1 a N,
e mostre o resultado obtido.'''

numero_final = eval(input('informe um numero--->' ))
resultado = 0
for numero in range(1,numero_final+1):
  resultado=resultado+numero
print(resultado)    
