#7.1
import numpy as np

nomes = ['ian', 'antonio','joao', 'jose', 'ian', 'joao', 'ian']
nomes.sort() #ordena

tam_vetor = np.size(nomes) #conta o tamanho do vetor

repeti = dict()#dicionário
tudo = list()

repeti["nome"]= nomes[0]
repeti["cont"]=1

tudo.append(repeti.copy())

atual=int(0)

for i in range(1,tam_vetor):
    if(tudo[atual]['nome']==nomes[i]):
        tudo[atual]['cont']+=1;
    else:
        repeti["nome"]= nomes[i]
        repeti["cont"]=1

        tudo.append(repeti.copy())
        atual+=1

for i in tudo:
    print();
    for x in i.values():
        print(x, end='');

#7.2
import numpy as np

nomes = []

while(1):
    nome = str(input('Digite um nome'))
    if(nome!=''):
        nomes.append(nome)
    else: 
        break

nomes.sort() #ordena

tam_vetor = np.size(nomes) #conta o tamanho do vetor

#dicionário
repeti = dict()
tudo = list()

repeti["nome"]= nomes[0]
repeti["cont"]=1

tudo.append(repeti.copy())

atual=int(0)

for i in range(1,tam_vetor):
    if(tudo[atual]['nome']==nomes[i]):
        tudo[atual]['cont']+=1;
    else:
        repeti["nome"]= nomes[i]
        repeti["cont"]=1

        tudo.append(repeti.copy())
        atual+=1

for i in tudo:
    print();
    for x in i.values():
        print(x,"  ", end='');

#7.3
import numpy as np

frase = str(input("Digite a frase que deseja marcar os nomes:"))

frase_array = frase.split()

tam = np.size(frase_array)

final = str()

for i in range(tam):
    if(frase_array[i].islower()==False):
        frase_array[i]=frase_array[i].replace(frase_array[i],'*')

for i in range(tam):
    final+= ' ' + frase_array[i]

if(frase.islower() == False):

    print(final)

else:
    print("A frase digitada não possui nomes!!!")

#7.4
import numpy as np

num= int(0)
A = list(); 
B = list();

for i in range(6):
    if (i<3):
        num = int(input("Digite o valor para o vetor A"));
        A.append(num);
    else:
        num = int(input("Digite o valor para o vetor B"));
        B.append(num);

print(A,"\n",B)


escalar = np.dot(A,B); #Pode ser feito assim escalar = (A[0]*B[0])+(A[1]*B[1])+(A[2]*B[2])

print("Escalar",escalar)

vetorial = np.cross(A,B) #A outra forma to com preguiça de fazer

print("Vetorial",vetorial)

#7.5
import numpy as np

N = int(input("Digite o tamanho do vetor N"))

lisata_N = list()

for i in range(N):
    inteiro = input("Digite um valar para vetor N:")
    lisata_N.append(inteiro)

print(lisata_N)

#7.6
import numpy as np

soma = media = int(0);

N = int(input("Digite o tamanho do vetor N"))

lisata_N = list()

for i in range(N):
    inteiro = int(input("Digite um valar para vetor N:"))
    lisata_N.append(inteiro)

maior = menor = lisata_N[0]

for i in range(N):
    
    soma += lisata_N[i];

    if(menor >= lisata_N[i]):
        menor = lisata_N[i];

    if(maior <= lisata_N[i]):
        maior = lisata_N[i];

media += soma/N

print("\nSoma: {0}\nMédia: {1}\nMaior: {2}\nMenor: {3}".format(soma,media,maior,menor))