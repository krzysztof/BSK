# Author: Krzysztof Nowak (kiryx7 [ at ] gmail.com)
#
# USAGE:
# ciphering: python railfence.py 4 "It's not dead, It's resting." > cipher.txt

import sys
height = int(sys.argv[1]);
message = sys.argv[2];
cipher = "";

a = height*2-2; #wartosc pierwszego skoku w kroku 0
b = 0;

tab_len = len(message); #max indeks

for k in range(height): #wykonaj sie height razy
	i = k;
	if(tab_len>i): #dopisujemy pierwsza litere
		cipher += message[i];
	while(True): #do konca wiersza dopisujemy na zmiane litere z idx i+a i i+b
		if(a>0):
			i+=a;
			if(tab_len>i):
				cipher += message[i];
			else:
				break;
		if(b>0):
			i+=b;
			if(tab_len>i):
				cipher += message[i];
			else:
				break;
	a-=2;
	b+=2;
		
print cipher;
