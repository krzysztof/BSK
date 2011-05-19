from strumieniowe import cycle
import sys
seed = [int(x) for x in list(sys.argv[1])]
wiel = [int(x) for x in sys.argv[2].split('-')]
N = int(sys.argv[3])
print "Org Seed:"+str(seed)
for i in range(N):
	seed = cycle(seed,wiel);
	print str(i+1)+"th Seed:"+str(seed)
#print seed, wiel
