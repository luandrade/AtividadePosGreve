valorPrestação = 1
relatorio = []
while (valorPrestação != 0 ):
  valorPrestação = eval(input('valor da prestação ---> '))
  diasAtrasados = eval(input('dias atrasados ---> '))
    
  def valorPagamento (valorPrestação, diasAtrasados):
   
    if diasAtrasados == 0:
      return valorPrestação
                         
    else:
      multa = 0.03 * valorPrestação
      juros = 0.001 * diasAtrasados
      totalAtraso = (multa + juros) + valorPrestação
      return totalAtraso
    
  print(valorPagamento(valorPrestação, diasAtrasados))
  relatorio.append(valorPagamento(valorPrestação, diasAtrasados))
else:
  print(relatorio)
