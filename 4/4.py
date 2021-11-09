#6.1
n = int(input("digite um valor para n: "));

primeiro = int(1)
segundo = int(0);
prite = int(0);

if(n==0): print("não possui valor")
elif(n==1): print("0");
elif(n>=2): 
    print("0");
    print("1");
    for i in range(n-2):
        prite = primeiro+segundo;
        segundo = primeiro;
        primeiro = prite;
        print(prite,"\t");
else: print("Erro numero não possivel na sequancia.")

#6.2
calcule = int(9);
resposta = int(1);

for i in range(calcule):
    resposta *= i+1;

print("A resposta de 9! é: ",resposta);

#6.3
calcule = int(9);
resposta = int(1);
i = int(0);

while(i < calcule):
    resposta *= i+1;
    i += 1;

print("A resposta de 9! é: ",resposta);

#6.4
soma = subt =mult = div = 0;

x= int(input("Escolha entre:\n1)soma\n2)subt\n3)mult\n4)div\n"));

Val1= float(input("Digite o primeiro valor a ser usado:  "));
Val2= float(input("Digite o segundo valor a ser usado:  "));

if (x==1): 

    soma = Val1+Val2;
    print("soma",soma);

elif (x==2): 

    subt = Val1-Val2;
    print("subt",subt);

elif (x==3): 

    mult = Val1*Val2;
    print("mult",mult);

elif (x==4): 

    div = Val1/Val2;
    print("div",div);

else :
    print ("Erro");

#6.5
calcule = int(input("Digite o numer que deseja achar o fatorial:  "));
resposta = int(1);
i = int(0);

while(i < calcule):
    resposta *= i+1;
    i += 1;

print("A resposta de {0}! é: {1}".format(calcule,resposta));

#6.6

#Pode ser utilizado desta forma:

#    if (x==1): 
#        foo (10) ;
#    elif (x==2): 
#        foo2 ( X ) ;
#    elif (x==3): 
#        foo (5) ;
#    else :
#        print ('Erro');