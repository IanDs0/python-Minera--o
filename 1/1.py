import math

olá= int(input('Digite o angulo'));
print ('O angulo digitado foi:\t',olá);

rad = (olá*3.14)/180;

print("\nrad: ",rad,"\ncos: ",math.cos(olá),"\nsen: ",math.sin(olá),"\ntg: ",math.tan(olá));

import numpy as np

olá= int(input('Digite o angulo'));

print(np.deg2rad(90));