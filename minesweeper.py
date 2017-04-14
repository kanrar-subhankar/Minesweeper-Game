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
def pos_generator(pos,n):
	if(pos%n==1):
		start=pos-n
	elif(pos%n==0 and pos!=n):
		start=pos-(n+2)
	elif(pos<n):
		start=pos
	else:
		start=pos-(n+1)
	return start
def diagonal(n,p):
	s=pos_generator(p,n)
	x,y=position_find(p)
	r,c=position_find(s)
	z=p
	count=0
	for i in range(r,r+3):
		for j in range(c,c+3):
			if [i,j] in pos_mines[:][:]:
				count+=1
	if count!=0:
		main_matrix[x][y]=count
		return 
	else:
		main_matrix[x][y]=' '
		u=z+n+1
		z=u;
		if(z!=n*n):
			diagonal(n,u)
		else:
			return
			
def traverse(main_matrix,pos_mines,n,p):
	s=pos_generator(p,n)
	x,y=position_find(p)
	r,c=position_find(s)
	count=0
	flag=0
	for i in range(r,r+3):
		for j in range(c,c+3):
			if [i,j] in pos_mines[:][:]:
				count+=1
	if count!=0:
		main_matrix[x][y]=count
		return 
	else:
		main_matrix[x][y]=' '
		diagonal(n,p)
		
				
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
for x in range(mines):
	li2=[]
	for j in range(2):
		x=random.randint(1,n-1)
		li2.append(x)
	pos_mines.append(li2)
print pos_mines		
for i in range(n):
	for j in range(n):
		print "\t",main_matrix[i][j],
	print 

while(True):
	x=input("Enter 0 to exit...")
	if(x==0):
		exit(0)
	else:
		sum=1
		for k in range(n):
			for l in range(n):
				str1='('
				str2=')'
				str_total=str1+str(sum)+str2
				main_matrix[k][l]=str_total
				sum+=1

		pos=int(input("Enter the number where you want to go!!!"))
		x,y=position_find(pos)
		
		##IF ENTER AT THE BOMB POSITION
		if [x,y] in pos_mines[:][:]:
			print "PLAY AGAIN"
			exit(0)
		else:
			
			traverse(main_matrix,pos_mines,n,pos)
			
			for i in range(n):
				for j in range(n):
					print "\t",main_matrix[i][j],
				print 
