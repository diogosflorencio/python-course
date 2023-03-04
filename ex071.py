valor_do_saque = int(input('Quanto vc quer sacar? '))
notas50 = valor_do_saque // 50
notas20 = (((valor_do_saque % 50)/50)*50)//20
notas10 = (((valor_do_saque % 20)/20)*20)//10
notas1 = (((valor_do_saque % 10)/10)*10)//1
print(f'{notas50} notas de 50,totalizando R${notas50*50:.2f};\n'
      f'{notas20} notas de 20, totalizando {notas20*20:.2f};\n'
      f'{notas10} notas de 10, totalizando {notas10*10:.2f};\n'
      f'{notas1} notas de 1 totalizando {notas1:.2f}.')
                                                                              