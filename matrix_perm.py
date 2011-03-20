# Author: Krzysztof Nowak (kiryx7 [ at ] gmail.com)
#
# USAGE:
# ciphering: python matrix_perm.py c 4-3-1-2 "It's not dead, It's resting." > cipher.txt
# deciphering: python matrix_perm.py d 4-3-1-2 "$(cat cipher.txt)" > message.txt
#
# Key: 
# Can either consist of single permutation divided by dashes: 5-2-3-1-4 
# or a word: eg. CRYPTO transates to 1-4-6-3-5-2
# If key_length does not divide message_length without a reminder, program adds white space at the end of the message

import sys,string

def get_key(key_string): #wyciaganie klucza z argumentu
	if "-" in key_string: #jesli klucz zawiera '-', else jesli jest slowem
		return [ int(x)-1 for x in key.split('-') ] #zamieniam "3-1-2" na tablice intow [3,1,2] (przy okazji-1 wszystko)
	else:
		key = list(key_string.upper());
		idx = 0;
		for i in string.ascii_uppercase:
			k = -1
			try:
				while True:
					k = key.index(i,k+1)
					key[k]=idx;
					idx += 1;
			except ValueError:
				pass
		return key
			
def reverse_key(key):
	new = list(key);
	for c in range(len(key)):
		new[key[c]]=c;
	return new
key = sys.argv[2];

key = get_key(key);

if(sys.argv[1]=='d'):
	key = reverse_key(key);	
N = len(key) #rozmiar tablicy, zeby nie czytac w petli
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
