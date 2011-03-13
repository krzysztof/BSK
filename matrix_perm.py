import sys
key = sys.argv[1];
key = [ int(x)-1 for x in key.split('-') ] #zamieniam "3-1-2" na tablice intow [3,1,2] (-1 wszystko)
N = len(key)#rozmiar tablicy, zeby nie czytac w petli
message = list(sys.argv[2])
while(len(message)%N != 0):
	message.append('_')#jesli zostaja puste pola w macierzy, wstawiamy spacje
#print message
tab_len = len(message)
cipher = list(message) #kopiuje tablice zeby odrazu miec indeksy

for k in range(N):#dla N-kolumn 
	for j in range(k,tab_len,N):#wybierz indeksy z danej kolumny
		cipher[j] = message[(key[k]-k)+j];#i podmien w szyfrze przesuwajac indeks o wartosc klucza

print "".join(cipher)#dopisanie do stringa elementow listy (stworzenie stringa na wyjscie)
