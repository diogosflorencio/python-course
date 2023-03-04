termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
contador = 0
pa = termo - razao
while contador < 10:
    contador += 1
    pa = pa + razao
    print(pa)

