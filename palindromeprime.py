start=int(input('Enter the start point N: \n'))
end=int(input('Enter the end point M: \n'))
y=0
print('The palindromic primes are:')
for num in range(start,end+1):
    if(str(num)==str(num)[::-1]):
        if num==2:
            y=1
        else:
            for val in range(start,end+1):
                if num%val>0:
                    y=y+1 
            if y>0:
                print(num)
                

            
                