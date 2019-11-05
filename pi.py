print('Approximation of pi: 3.121')
r=eval(input('Enter the radius:\n'))
import math
deno=math.sqrt(2)
a=deno
b=math.sqrt(2+deno)
c=math.sqrt(2+b)
print('Area:',round((2*2/a*2/b*2/c)*(r**2),3))