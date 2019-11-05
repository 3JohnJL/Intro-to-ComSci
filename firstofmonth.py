import calendar
month=input('Enter the month: ')
if month=='January':
    mn=1
elif month=='February':
    mn=2
elif month=='March':
    mn=3
elif month=='April':
    mn=4
elif month=='May':
    mn=5
elif month=='June':
    mn=6
elif month=='July':
    mn=7
elif month=='August':
    mn=8
elif month=='September':
    mn=9
elif month=='October':
    mn=10
elif month=='November':
    mn=11
elif month=='December':
    mn=12
yr=eval(input('Enter the year: '))
first=calendar.monthrange(yr,int(mn))[0]
if first==0:
    first_day='Monday'
elif first==1:
    first_day='Tuesday'
elif first==2:
    first_day='Wednesday'
elif first==3:
    first_day='Thursday'
elif first==4:
    first_day='Friday'
elif first==5:
    first_day='Saturday'
elif first==6:
    first_day='Sunday'
print('The 1st of',month,yr,'is a',first_day,end='.')