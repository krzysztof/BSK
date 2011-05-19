import sys,operator
from strumieniowe import cycle
seed = [int(x) for x in list(sys.argv[2])]
wiel = [int(x) for x in sys.argv[3].split('-')]

if(sys.argv[1].upper() == 'C'):
	plik = open(sys.argv[4],"r")
	file_arr = []
	try:
		byte = plik.read(1)
		while(byte != ""):
			out_byte_new = 0
			byte=ord(byte)
			for b in [int(m) for m in bin(byte)[2:].zfill(8)]:		
				seed = cycle(seed,wiel)
				out_byte_new=out_byte_new<<1
				out_byte_new+=b^seed[0]
				seed[0]=b^seed[0]

			file_arr.append(out_byte_new)
			byte = plik.read(1)
	finally:
		plik.close()

elif(sys.argv[1].upper() == 'D'):
	plik = open(sys.argv[4],"r")
	file_arr = []
	try:
		byte = plik.read(1)
		while(byte != ""):
			out_byte_new = 0
			byte=ord(byte)
			for b in [int(m) for m in bin(byte)[2:].zfill(8)]:		
				seed = cycle(seed,wiel)
				out_byte_new=out_byte_new<<1
				out_byte_new+=b^seed[0]
				seed[0] = b
				#seed[0]=b^seed[0]
		

			file_arr.append(out_byte_new)
			byte = plik.read(1)
	finally:
		plik.close()

##zapis do pliku
plik = open(sys.argv[5],"w")
try:
	for i in file_arr:
		plik.write(chr(i))
finally:
	plik.close()
