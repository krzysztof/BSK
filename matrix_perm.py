# Author: Krzysztof Nowak (kiryx7 [ at ] gmail.com)
#
# USAGE:
# ciphering: python matrix_perm.py c 1-3-2 "It's not dead, It's resting." > cipher.txt
# deciphering: python matrix_perm.py d 1-3-2 "$(cat cipher.txt)" > message.txt
# If key_length does not divide msg_length without a reminder, program adds white space at the end of the message

import sys

def get_key(key_string):
	
	if "-" in key_string: #jesli klucz zawiera '-'
		key = [ int(x)-1 for x in key.split('-') ] #zamieniam "3-1-2" na tablice intow [3,1,2] (przy okazji-1 wszystko)
	else:
		key = list(key_string.upper());
		print key;
		#for i in range(len(key)):
			
def reverse_key(key):
	new = list(key);
	for c in range(len(key)):
		new[key[c]]=c;
	return new
key = sys.argv[2];

key = get_key(key);

if(sys.argv[1]=='d'):
	key = reverse_key(key);	
N = len(key)#rozmiar tablicy, zeby nie czytac w petli
message = list(sys.argv[3])
while(len(message)%N != 0):
	message.append(' ')#jesli zostaja puste pola w macierzy, wstawiamy spacje
#print message
tab_len = len(message)
cipher = list(message) #kopiuje tablice zeby odrazu miec indeksy

for k in range(N):#dla N-kolumn 
	for j in range(k,tab_len,N):#wybierz indeksy z danej kolumny
		cipher[j] = message[(key[k]-k)+j];#i podmien w szyfrze przesuwajac indeks o wartosc klucza

print "".join(cipher)#dopisanie do stringa elementow listy (stworzenie stringa na wyjscie)
