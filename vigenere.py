# Author: Krzysztof Nowak (kiryx7 [ at ] gmail.com)
#
# USAGE:
# ciphering: python vigenere.py c "KEYWORD" "SECRETSATANICMESSAGE" > cipher.txt
# deciphering: python vigenere.py d "KEYWORD" "$(cat cipher.txt)" > message.txt

import sys
option = sys.argv[1].upper();
keyword = sys.argv[2].upper();
message = sys.argv[3].upper();
cipher = "";

n = 26
key_idx = 0

if(option == 'C'):
	multiplier = 1;
elif(option == 'D'):
	multiplier = -1;

for letter in message:
	cipher += chr((ord(letter)+multiplier*ord(keyword[key_idx]))%n+65)
	key_idx+=1;
	key_idx%=len(keyword)

print cipher

