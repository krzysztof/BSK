# Author: Krzysztof Nowak (kiryx7 [ at ] gmail.com)
#
# USAGE:
# ciphering: python railfence.py c 4 "It's not dead, It's resting." > cipher.txt
# deciphering: python railfence.py d 4 "$(cat cipher.txt)" > message.txt

import sys
option = sys.argv[1];
height = int(sys.argv[2]);
message = sys.argv[3];
cipher = "";
tab_len = len(message); #max indeks
hill_size = height*2-2; #dlugosc jednego wzniesienia w plotku

if('C' in option.upper()):
	skok = [ hill_size, 0 ] #odleglosc skokow po wierszach
	idx_skok = 0; #pierwszy skok
	
	for k in range(height): #wykonaj sie height razy
		i = k;
		if(tab_len>i): #dopisujemy pierwsza litere
			cipher += message[i];
		while(True): #do konca wiersza dopisujemy na zmiane litere z idx i+a i i+b
			if(skok[idx_skok]>0):
				i+=skok[idx_skok];
				if(tab_len>i):
					cipher += message[i];
				else:
					break;
			idx_skok += 1;
			idx_skok %= 2;
		#po kazdym wierszu plotka zmieniamy wartosci skokow
		skok[0]-=2;
		skok[1]+=2;
		idx_skok=0;

elif('D' in option.upper()):
	group_cnt = tab_len/hill_size; #ilosc pelnych wzniesien
	a = [0]*height #ilosc grup == wysokosc
	a[-1] = a[0] = group_cnt; #licznosc w pierwszej i ostatniej grupie
	reminder = tab_len % hill_size;
		
	for i in range(len(a)): #do kazdej licznosci z grupy
		if(reminder > i): #sprawdzamy czy reszta 
			a[i] += 1;
		if(i>0 and i<(len(a)-1)):	
			a[i] += group_cnt*2; #licznosc w pozostalych
			if(reminder >= (2*height - i - 1)):
				a[i]+=1;
	prev = 0;
	for i in range(len(a)):
		tmp=message[prev:prev+a[i]]; #wyciagamy z tekstu kolejno wycinki (zgodnie z licznoscami w grupach)
		prev += a[i]
		a[i]=list(tmp)
	idx = 0;
	addition = 1;
	#print a
	for _ in range(tab_len):
		cipher+=a[idx].pop(0);
		#print cipher		
		idx += addition;
		if(idx>=height):
			addition=-1;
			idx-=2
		if(idx<0):
			addition=1;
			idx+=2;
		
print cipher;
