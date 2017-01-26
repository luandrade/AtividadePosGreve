''' 5) (Adaptado – Python Zumbi) Escreva um programa para calcular a redução de tempo
de vida de um fumante. Considere que para cada cigarro fumado por dia, durante o
tempo em anos que ele tem o hábito de fumar, ele perdeu 10 minutos de sua vida. Dessa
forma, exiba para o usuário o tempo de vida perdido com o hábito do fumo. '''

qtdAnos = eval(input("Há quantos anos você fuma? "))
qtdCigarros = eval(input("Quantos cigarros você fuma por dia? "))
qtdDias = qtdAnos * 365
cigarrosTotal = qtdCigarros * qtdDias
tempoPerdido = round((cigarrosTotal * 10) / 24)

print("Você já fumou", cigarrosTotal, "cigarros e perdeu", tempoPerdido, "dias da sua vida!")
