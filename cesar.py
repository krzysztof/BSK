# Author: Krzysztof Nowak (kiryx7 [ at ] gmail.com)
#
# Algorithm based on cesars cipher
#
# USAGE:
# ciphering: python cesar.py c 21 "SECRETMESSAGE" > cipher.txt
# deciphering: python cesar.py d 21 "$(cat cipher.txt)" > message.txt
from math import ceil, sqrt
def find_factor(n):
	a = range(int(ceil(sqrt(n))));
	a.reverse()
	for i in a:
		if(n%i==0):
			return (i,n/i);
	return -1;

import sys
option = sys.argv[1].upper();
key = int(sys.argv[2]);
message = sys.argv[3];
cipher = "";
n = 26

k = find_factor(key)
phi = (k[0]-1)*(k[1]-1)

if(option == 'C'):
	for letter in message:
		cipher += chr( ((ord(letter)-65)*k[1]+k[0])%n +65)
elif(option == 'D'):
	for letter in message:
		Ci = ord(letter)-65
		cipher += chr( ((Ci + (n-k[0]))*k[1]**(phi-1) )%n + 65)

print cipher

