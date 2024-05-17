import sys

graph={}

for line in sys.stdin:
	line=line.strip()
	key=line.split()
	node=key[0]
	edge=key[1]
	if node not in graph:
		graph[node]=set()
	graph[node].add(edge)
	
for i in graph:
	a=graph[i]
	stri=','.join(a)
	print('{}\t{}'.format(i,str(stri)))
