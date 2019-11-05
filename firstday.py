year=eval(input('Enter the year: '))
a=(year-1&4)
b=(year-1%100)
F=(year-1&400)
day=(1+a+b+F)%7
print('The 1st of January',year,'falls on day',day,'of the week.')
print('(0 is Sunday, 1 is Monday, ..., 6 is Saturday.)')