# JHNLYD001

print ('***** Program Trace Utility *****')
name = input ('Enter the name of the program file: ')
print ('Inserting...Done')

myfile = open(name, 'r+')

x=file.readlines()

myfile.close()

if x[0]=='"""DEBUG"""\n':
    x.remove(x[0])
elif x[0]!='"""DEBUG"""':
    x.insert(0, '"""DEBUG"""\n')

for i in range (len(x)):
    try:
        if x[i][0:3:1]=='def':
            if x[i+1][4:15:1]!='"""DEBUG"""':
                colon=x[i].find('(')
                name=x[i][4:(colon):1]
                insertfunc=str(' '*4+'"""DEBUG""";print(\''+ name + '\')\n')
                x.insert((i+1), insertfunc)
            elif x[i+1][4:15:1]=='"""DEBUG"""':
                x.remove(x[i+1])
    except:
        continue
 
myfile = open(name, 'w')        
        
for j in range (len(x)):
    myfile.write(x[j])
    
myfile.close()