s=input('Enter the raw data:\n')
l=s.find('BEGIN')
y=s.find('_')
d=s.find(':')
i=s.find(',')
a=s.find('END')
p=s[i+6:a-1]
lo=p[::-1]
ll=lo.lower()
print('Site information:')
print('Location:',ll.capitalize())
print('Coordinates:',s[i+1:i+6],s[d+1:i])
print('Temperature:',s[l+5:y],' C',sep='')
print('Pressure:',s[y+1:d],'hPa')

