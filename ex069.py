maiores = 0
mulheres_20 = 0
homens = 0
while True:
  idade = int(input('Qual a idade? '))
  while idade < 0 or idade > 150:
    idade = int(input('Qual a idade? '))
  sexo = input('Qual o sexo [H/M]? ').upper()[0].strip()
  while sexo != 'H' and sexo != 'M':
    sexo = input('Qual o sexo [H/M]? ').upper()[0].strip()
  if idade > 18:
    maiores +=1
  if sexo == 'H':
    homens +=1
  if sexo == 'M' and idade > 20:
    mulheres_20 +=1
  print('Cadastrado!')
  continuar = input('Deseja cadastrar mais? [S/N] ').upper()[0].strip()
  while continuar != 'S' and continuar != 'N':
    continuar = input('Deseja cadastrar mais? [S/N] ').upper()[0].strip()
  if continuar == 'N':
    print(f'{maiores} pessoas têm mais de 18 anos!\n {homens} homens cadastrados!\n {mulheres_20} mulheres com mais de 20 anos!')
    break
  else:
    print()