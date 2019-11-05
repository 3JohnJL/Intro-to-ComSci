userTime=input('Enter time ([h]h:mm am|pm): ')
evaluate=userTime.find('m')
seg=eval(userTime[:userTime.find(':')])
if userTime[evaluate-1]=='p' and seg<12:
    change=seg+12
    print(change,userTime[userTime.find(':'):userTime.find(':')+3],sep='')
elif userTime[evaluate-1]=='p' and seg==12:
    print(userTime.replace('pm',''))
elif userTime[evaluate-1]=='a' and seg==12:
    new=(userTime.replace('12','00'))
    print(new.replace('am',''))
else:
    print('0',userTime.replace('am',''),sep='')