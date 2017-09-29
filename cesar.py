# Author: Krzysztof Nowak (kiryx7 [ at ] gmail.com)
#
# Algorithm based on cesars cipher 
#
# USAGE:
# ciphering: python cesar.py c 9 11 "Secret Message" > cipher.txt
# deciphering: python cesar.py d 9 11 "$(cat cipher.txt)" > message.txt
from math import ceil, sqrt
def tocjent(n):
	#max_size = int(ceil(sqrt(n)))
	max_size = n+1;
	#max_size = n
	primes = range(2,max_size) #nie moge od pierwiastka ani /2 bo n moze byc pierwsze
	for i in range(len(primes)):
		if(primes[i]!=-1):
			j=i+primes[i]
			while(j<len(primes)):
				primes[j]=-1;
				j+=primes[i];
	primes = [x for x in primes if (x!=-1 and n%x==0)]
	wynik = n;
	mianownik = 1;
	for x in primes:
		wynik*=(x-1);
		mianownik*=x;
	return wynik/mianownik;
	#print primes
	#print "tocjent:",wynik/mianownik;


import sys,string
option = sys.argv[1].upper();
k=[1,1];
k[0] = int(sys.argv[2]);
k[1] = int(sys.argv[3]);
message = sys.argv[4];
cipher = ""
alfabet = string.ascii_letters+' -,\'1234567890_.:\n\t'; #tworzymy alfabet A-Za-z z jakimis krzakami
n = len(alfabet)
if(n%k[0]==0):
	print "k0 nie jest pierwsze z n"
elif(n%k[1]==0):
	print "k1 nie jest pierwsze z n"
mapa = dict( zip(alfabet , range(n)) ) #tworzymy hash-mape par 'a':0 'b':1 itd..
#print mapa
#print len(mapa)
fi = tocjent(n)
#	print i,":",tocjent(i)

if(option == 'C'):
	for letter in message:
		cipher += alfabet[((mapa[letter])*k[1]+k[0])%n]
elif(option == 'D'):
	for letter in message:
		Ci = mapa[letter]
		cipher += alfabet[((Ci + (n-k[0]))*(k[1]**(fi-1)))%n]

print cipher

