words=[]
strings=input('Enter strings (end with DONE):\n')
align=0
if len(strings)>align:
    words.append(strings)
while strings !='DONE':
    strings=input()
    if strings=='DONE':
        break
    else:
        strings.format('>')
        words.append(strings)
        if len(strings)>align:
            align=len(strings)
print()
print('Right-aligned list:')
length=len(words)
for i in range(length):
    print(words[i].rjust(align))