num=int(input('Enter a number: \n'))
y=0
if num==2:
    y==0
else:
    for val in range(2,num):
        if num%val==0:
            y=y+1
if y>0:
    print('Number is not prime')
else:
    print('Number is prime')
