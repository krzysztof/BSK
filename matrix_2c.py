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

option = sys.argv[1].upper();
key = sys.argv[2];
key = get_key(key);
message = sys.argv[3]
cipher = "";

rows = int(len(message)*len(key));
tab = [ len(key)*[0] for _ in range(rows) ]
tab = set_matrix(key,tab,len(message));

if(option.upper() == 'C'):
	mes_idx = 0;
	key=reverse_key(key);
	for i in range(len(tab)):
		for j in range(len(tab[0])):
			if(tab[i][j]==1):
				tmp = message[mes_idx];
				tab[i][j]=tmp;
				mes_idx+=1;
#	for i in tab:
#		for j in i:
#			print j,
#		print '\n'
	
	for j in key:
		for i in range(len(tab)):
			if(tab[i][j]!=0):
				cipher+=tab[i][j];
				
	
elif(option.upper() == 'D'):
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

