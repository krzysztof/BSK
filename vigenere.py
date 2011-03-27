# Author: Krzysztof Nowak (kiryx7 [ at ] gmail.com)
#
# Algorithm based on vigenere table.
#
# USAGE:
# ciphering: python vigenere.py c "KEYWORD" "Secret Message number 23" > cipher.txt
# deciphering: python vigenere.py d "KEYWORD" "$(cat cipher.txt)" > message.txt

import sys,string
option = sys.argv[1].upper();
keyword = sys.argv[2];
message = sys.argv[3];
cipher = "";

key_idx = 0

alfabet = string.ascii_letters+' -1234567890_.:\n\t'; #tworzymy alfabet A-Za-z z jakimis krzakami
n = len(alfabet);
mapa = dict( zip(alfabet , range(n)) ) #tworzymy hashmape par 'a':0 'b':1 itd..
if(option == 'C'):
	multiplier = 1;
elif(option == 'D'):
	multiplier = -1;

for letter in message:
	cipher += alfabet[ (mapa[letter] + multiplier*mapa[keyword[key_idx]] ) % n ];
	key_idx+=1;
	key_idx%=len(keyword);

print cipher

