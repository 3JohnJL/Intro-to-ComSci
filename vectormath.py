import math                           #allows for the use of functions in the math library such as 'sqrt'

a=input('Enter vector A:\n')
A=[]
B=[]
c=[]
for i in range(3):
    c.append(0)
def hold(d,e,f):
    A.append(d)
    A.append(e)
    A.append(f)
    
def bhold(j,k,l):
    B.append(j)
    B.append(k)
    B.append(l)
d,e,f=(int(j) for j in a.split())
hold(d,e,f)
b=input('Enter vector B:\n')
j,k,l=(int(d) for d in b.split())
bhold(j,k,l)

c[0]=A[0]+B[0]
c[1]=A[1]+B[1]
c[2]=A[2]+B[2]

print('A+B =',c)
print('A.B =',(A[0]*B[0])+(A[1]*B[1])+(A[2]*B[2]))
print('|A| =',round(math.sqrt(A[0]**2+A[1]**2+A[2]**2),2))
print('|B| =',round(math.sqrt(B[0]**2+B[1]**2+B[2]**2),2))