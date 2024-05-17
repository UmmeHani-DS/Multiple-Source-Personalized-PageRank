import sys
import csv

def findPR(graph,node,P):
	temp=set()
	
	for i in graph:
		if node in graph[i]:
			temp.add(P[i]/len(graph[i]))
	res=sum(temp)
	return res
	


graph={}

for line in sys.stdin:
	line=line.strip.split('\t')
	if len(line) >=2:
		node=line[0]
		graph[node] = line[1].split(',')
		
		



num=68373777

PR={}

for i in graph:
	
	if i == 1665:
		PR[i]=1/3
	elif i == 1715:
		PR[i]=1/3
	elif i == 1781:
		PR[i]=1/3
        else: 
		PR[i] = 0
	

for i in graph:
	a=findPR(graph,i,PR)
	PR[i]=a
	
	
print(PR)
