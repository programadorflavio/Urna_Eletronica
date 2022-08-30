print('''
eleição 2022
[1] - [nulo]
[2] - [Lula]
[3] - [Bolsonaro]
[4] - [Ciro]
[111] - [Encerrar]
      ''')
voto = nulo = bolsonaro = lula = ciro = 0
cont = 1
while voto != 111:
    voto = int(input('próximo eleitor, qual seu voto [111 - para encerrar as votações]:'))
    cont += 1
    if voto == 1:
        nulo += 1
        print('voto nulo registrado com sucesso')
    if voto == 2:
        lula += 1
        print('voto em Lula registrado com sucesso.')
    if voto == 3:
        bolsonaro += 1
        print('voto em Bolsonaro registrado com sucesso.')
    if voto == 4:
        ciro += 1
        print('Voto em Ciro registrado com sucesso.')
    if voto != 1 and voto != 2 and voto != 3 and voto != 4:
        print('opção inválida, tente novamente.')
        cont -= 1


maior = nulo
menor = nulo

if lula > maior:
    maior = lula
if bolsonaro > maior:
    maior = bolsonaro
if ciro > maior:
    maior = ciro

print(f'''
FIM DAS ELEIÇÕES 2022
HOUVERAM {cont -1} ELEITORES PRESENTES
os resultados foram nulo: {nulo} - Lula:{lula} - Bolsonaro:{bolsonaro} - Ciro:{ciro} 

''')