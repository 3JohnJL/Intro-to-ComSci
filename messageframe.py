message=input('Enter the message:\n')
repeat=int(input('Enter the message repeat count:\n'))
width=int(input('Enter the frame thickness:\n'))
for i in range(0,width):
    print('|'*i,'+','-'*((len(message)+2*width)-(2*i)),'+','|'*i,sep='')
for l in range(repeat):
    print('|'*width,message,'|'*width)
for j in range(0,width):
    p=-(j-width+1)
    print('|'*p,'+','-'*((len(message)+2*width)-(2*p)),'+','|'*p,sep='')
