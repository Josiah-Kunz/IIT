f=open('distrib.dat','w')
f.write('#\n')
f.write('#x y z Px Py Pz t PDGid EventID TrackID ParentID Weight\n')
a=[]
with open('for004.dat','r') as f2:
	for line in f2:
		a.append(line.split('\t')[0])


f.close
