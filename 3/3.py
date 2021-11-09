import math

Valor = float(input('Valor a ser sacado'));

print("\n O valor a ser sacado é de ",Valor);

cem = Valor /100;
Valor = Valor % 100;

cinquenta = Valor/50;
Valor = Valor %50;

dez = Valor/10;
Valor = Valor %10;

um =Valor;

print("\n O numero de notas 100: ", math.floor(cem));
print("\n O numero de notas 50: ", math.floor(cinquenta));
print("\n O numero de notas 10", math.floor(dez));
print("\n O numero de notas 1: ", math.floor(um));

##
import math

Temp = int(input("Digite o numero de segundo sque deseja converter para horas,minutos, sehundos"));

print("O tempo inicial em segundos é de {}",Temp);

horas = Temp/3600;
Temp %= 3600;

minutos = Temp/60;
Temp %= 60;

segundos= Temp;

print("\n O numero de Horas: ",math.floor(horas));
print("\n O numero de minutos: ",math.floor(minutos));
print("\n O numero de segundos: ",math.floor(segundos));

##
import math

Val1= float(input("Digite o primeiro valor a ser usado:  "));
Val2= float(input("Digite o segundo valor a ser usado:  "));

soma = Val1+Val2;
subt = Val1-Val2;
mult = Val1*Val2;
div = Val1/Val2;

print("Primeiro valor: ",Val1,"\nSegundo valor: ",Val2);

print("\nSoma: ",soma,"\nSubtração: ",subt,"\nMultiplicação: ",mult,"\nDivisão: ",div);