#author: kiryx7 [at] gmail.com
import sys,copy,struct

alpha_size = 256;
offsets = []

def reverse_perm(perm): #odwracanie permutacji
	new = list(perm);
	for c in range(len(perm)):
		new[perm[c]]=c;
	return new

N = int(sys.argv[1]);
	
def generate_perms(key):
	out = []
	for _ in range(N):
		out.append(range(alpha_size));
	key_l = [ ord(x) for x in key ]
	out2 = copy.deepcopy(out);
	for p in range(N):
		offsets.append( (p*key_l[p*p % len(key_l)] + p) % alpha_size );
		#offsets.append(0)
	for p in range(N):
		for i in range(alpha_size):
			new_idx = ((i+1)*key_l[i % len(key_l)]*(p+1)**3) % len(out[p]);
#			print len(out[p]),":",len(out2[p]),":",new_idx
			out2[p][i] = out[p][new_idx];
			del out[p][new_idx];
	
	out2.append( [alpha_size -1 - i for i in range(alpha_size) ] )

	r = range(N);
	r.reverse();
	for p in r:
		out2.append(reverse_perm(out2[p]));
	return out2;
def inc_and_check(i):
	offsets[i]+=1;
	if(offsets[i]>=alpha_size):
		offsets[i]=0;
		if(i+1<len(offsets)):
			inc_and_check(i+1);
		
def increment_offsets():
	inc_and_check(0);	
	
def read_file(file):
	file_arr = []
	f = open(file,"rb")
	try:
		byte = f.read(1)
		while( byte != ""):
			#file_arr.append(struct.unpack('i',byte)[0])
			file_arr.append(ord(byte));
			#print ord(byte)
			byte = f.read(1)
	finally:
		f.close()
	return file_arr


def write_file(file,file_arr):
	f = open(file,"wb")
	try:
		for i in file_arr:
			f.write(chr(i))
	finally:
		f.close()

def cipher_file(file_arr):
	file_arr2 = []
	for i in file_arr:
		file_arr2.append(cipher_byte(i,perm_list,False))
		increment_offsets()
	return file_arr2

def cipher_byte(byte,perm_list,verbose):
	#pierwsze permutacje
	if(verbose):
		print "In:",byte
	for p in range(len(perm_list)/2):
		pre = byte;
		byte = perm_list[p][(byte + offsets[p]) % alpha_size]
		if(verbose):
			print "P :",p,"|O:",offsets[p],":",pre,"->",byte

	#reflektor
	p = len(perm_list)/2;
	pre = byte
	byte = perm_list[p][byte];
	if(verbose):
		print "R :",p,"       ",pre,"->",byte

	#odwrotne
	for p in range(len(perm_list)/2+1,len(perm_list)):
		off_idx = N - p
		lp = alpha_size
		pre = byte;
		p_rev = perm_list[p];
		p_orig = perm_list[p-(len(perm_list)/2+1)];
		byte = (p_rev[byte] - offsets[off_idx] )% alpha_size
		if(verbose):
			print "P':",p,"|O:",offsets[off_idx],":",pre,"->",byte

	return byte;
	
	
key = sys.argv[2];

filein = sys.argv[3];
fileout = sys.argv[4];
perm_list = generate_perms(key);

verbose = False;
if(verbose):
	print "offsets:",offsets
	print "perms:"
	
	for p in range(len(perm_list)): 
		print p,":",perm_list[p],
		if(p<len(offsets)):
			print "off:",offsets[p]
		else:
			print ""
	print "\n"

a = read_file(filein)
b = cipher_file(a);
write_file(fileout,b)
