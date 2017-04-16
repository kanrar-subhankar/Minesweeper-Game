#import numpy as np #numpy module
import random

def position_find(pos):
	if(pos%n==0):
		x=(pos/n)-1
	else:
		x=(pos/n)
	if(pos%n==0):
		y=n-1
	else:
		y=(pos%n)-1
	return x,y
					
def traverse(n,x,y):
	count=0
	flag=0
	for i in range(x-1,x+2,1):
			for j in range(y-1,y+2,1):
				if(i<n and j<n and i>=0 and j>=0):
					if [i,j] in pos_mines[:][:]:
						count+=1
	if count!=0:
		main_matrix[x][y]=count
		return 
	else:
		main_matrix[x][y]=' '
		#full_traverse(s)
		for i in range(x-1,x+2,1):
			for j in range(y-1,y+2,1):
				if(i<n and j<n and i>=0 and j>=0 and main_matrix[i][j]!=' '):
					traverse(n,i,j)
		
				
#numpy can declare a matrix as np.arange(100).reshape(10*10)
num=1
n=int(input("Enter size of matrix::")) 
main_matrix=[]
for i in range(n):
	li=[]
	for j in range(n):
		str1='('
		str2=')'
		concat=str1+str(num)+str2
		li.append(concat)
		num+=1
	main_matrix.append(li)
	
mines=int(input("Enter the no of Mines::"))

pos_mines=[]
for low in range(mines):
	li2=[]
	for j in range(1):
		ty1=random.randint(0,n-1)
		ty2=random.randint(0,n-1)
		if([ty1,ty2] not in pos_mines[:][:]):
			li2.append(ty1)
			li2.append(ty2)
			pos_mines.append(li2)
		else:
			j=0
			
for i in range(n):
	for j in range(n):
		print "\t",main_matrix[i][j],
	print 

while(True):
	x=input("Enter 0 to exit...")
	if(x==0):
		exit(0)
	else:

		pos=int(input("Enter the number where you want to go!!!"))
		x,y=position_find(pos)
		
		##IF ENTER AT THE BOMB POSITION
		if [x,y] in pos_mines[:][:]:
			for l in range(len(pos_mines)):
				ax1=pos_mines[l][0]
				ax2=pos_mines[l][1]
				main_matrix[ax1][ax2]='*'
			for m in range(n):
				for r in range(n):
					print "\t",main_matrix[m][r],
				print 
			print "PLAY AGAIN"
			exit(0)
		else:
			traverse(n,x,y)
			for i in range(n):
				for j in range(n):
					print "\t",main_matrix[i][j],
				print 
