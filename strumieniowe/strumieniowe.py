def cycle(s,w):
	out = 0
	for pol in w:
		#print str(s[pol])+"("+str(pol)+")",
		out^=s[pol]
	#print " xor: ",out
	out_seed = s[:-1]
	out_seed.insert(0,out)
	return out_seed	
