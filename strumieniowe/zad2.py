import sys,operator
LUT = [0,255]
from strumieniowe import cycle
seed = [int(x) for x in list(sys.argv[1])]
wiel = [int(x) for x in sys.argv[2].split('-')]

##odczyt z pliku
plik = open(sys.argv[3],"r")
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
		

		file_arr.append(out_byte_new)
		byte = plik.read(1)
finally:
	plik.close()

##zapis do pliku
plik = open(sys.argv[4],"w")
try:
	for i in file_arr:
		plik.write(chr(i))
finally:
	plik.close()
