# Author: Krzysztof Nowak (kiryx7 [ at ] gmail.com)
#
# USAGE:
# ciphering: python matrix_2c.py c CONVENIENCE "It's not dead, It's resting." > cipher.txt
# deciphering: python matrix_2c.py d CONVENIENCE "$(cat cipher.txt)" > message.txt
#
# Key: 
# Can either consist of single permutation divided by dashes: 5-2-3-1-4 
# or a word: eg. CRYPTO transates to 1-4-6-3-5-2

import sys,string
from math import ceil

def get_key(key_string): #wyciaganie klucza z argumentu
	if "-" in key_string: #jesli klucz zawiera '-', else jesli jest slowem
		return [ int(x)-1 for x in key_string.split('-') ] #zamieniam "3-1-2" na tablice intow [3,1,2] (przy okazji-1 wszystko)
	else:
		key = list(key_string.upper());
		idx = 0;
		for i in string.ascii_uppercase: #po kolei wszystlie litery z alfabetu ascii_uppercase [A-Z]
			k = -1
			try:
				while True: #chcemy znalezc wszystkie wystapienia kazdej z liter (i) w kluczu
					k = key.index(i,k+1) #szukamy indeksu wystapienia zaczynajac od k+1 (poczatkowo k=-1, zatem od 0)
					key[k]=idx; #jesli znajdziemy litere k zastepujemy kolejnym indeksem (mamy permutacje)
					idx += 1;
			except ValueError: #jesli 3 linijki wyzej nie ma wiecej liter, rzuca wyjatek ktory zostawiamy
				pass
		return key
			
def reverse_key(key): #odwracanie permutacji
	new = list(key);
	for c in range(len(key)):
		new[key[c]]=c;
	return new

def set_matrix(key,matrix,message_len):
	counter = 0;
	real_i = len(matrix)-1;
	for i in range(len(matrix)):
		jump = key.index(i%len(key));
		for j in range(jump+1):
			if(counter == message_len):
				real_i = i;
				counter+=1;
			elif(counter > message_len):
				pass
			else:
				matrix[i][j]=1;
				counter+=1;
	return matrix[:real_i+1]


key = sys.argv[2];
option = sys.argv[1].upper();
key = get_key(key);

#if(sys.argv[1]=='d'):
	#key = reverse_key(key);	
N = len(key) #rozmiar tablicy, zeby nie czytac w petli
message = sys.argv[3]
out_matrix = []
cipher = "";
out_str = ""
k=0;
key_idx = 0;
if(option.upper() == 'C'):
	#spisujemy wiadomosc do macierzy
	#sprawdzajac czy nalezy przeniesc wiadomosc do kolejnej tablicy
	
	for idx in range(len(message)):
		out_str+=message[idx];
		if(key_idx<len(key) and key[key_idx]==k):
			out_matrix.append(out_str);
			k+=1;
			key_idx=0;
			out_str=""
		#elif (key_idx>=len(key)-1):
		#	key_idx=0;
		#	out_matrix.append(out_str);
		#	out_str=""
		else:
			key_idx+=1;
			key_idx%=len(key);
	out_matrix.append(out_str);
	out_str2 = ""
	i = 0;
	j = 0;
	out_matrix2 = []
	tmp_counter = 0;
	#zapisujemy wiadomosc kolumnami
	while(len(message)>tmp_counter):
		if(i<len(out_matrix) and j<len(out_matrix[i])):
			tmp_counter +=1;
			out_str2+=out_matrix[i][j];
		i+=1;
		if(i==len(out_matrix)):
			out_matrix2.append(out_str2);
			out_str2=""
			i=0;
			j+=1;
	out_matrix2.append(out_str2);
	out_matrix3 = list(out_matrix2)
	
	for i in range(len(key)):
		out_matrix3[key[i]]=out_matrix2[i];
			
	cipher = cipher.join(out_matrix3);
		
	#print out_matrix3;
	#print out_matrix2;
elif(option.upper() == 'D'):
	rows = int(ceil((len(message)+ ((len(key)*(len(key)-1))/2))/len(key)))
	tab = [ len(key)*[0] for _ in range(rows) ]

	tab = set_matrix(key,tab,len(message));
#	for i in tab:
#		for j in i:
#			print j,
#		print '\n'
	mes_idx = 0;
	#print key
	#for j in range(len(tab[0])):
	key = reverse_key(key)
	for j in key:
		for i in range(len(tab)):
			if(tab[i][j]==1):
				tmp = message[mes_idx];
				tab[i][j]=tmp	
				mes_idx+=1;
#	for i in tab:
#		for j in i:
#			print j,
#		print '\n'
	for i in range(len(tab)):
		for j in range(len(tab[0])):
			if(tab[i][j]!=0):
				cipher+=tab[i][j];
			
print cipher;
#print out_matrix

