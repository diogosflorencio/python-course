VDC = int(input('Qual o valor da diária deste aluguel? '))
VKMC = float(input(' Qual custo no aluguel por KM rodados? '))
D = int(input('quantos dias vc ficou com o carro? '))
KM = float(input('quantos kilometros vc andou com o carro? '))
VKM = KM*VKMC
VD = D*VDC
VKMD = VKM+VD
print(f'custando cada dia com o carro ${VDC} e ${VKMC} por cada KM, o valor total do aluguel, será dê: ${VKMD}')