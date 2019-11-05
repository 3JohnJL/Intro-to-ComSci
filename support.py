def welcome():
    print('Welcome to the automated technical support system.')
    print('Please describe your problem:')

def get_input():
    return input().lower()


def main():

    welcome()    
    query = get_input()
    support={'crashed':'Are the drivers up to date?','blue':'Ah, the blue screen of death. And then what happened?','hacked':'You should consider installing anti-virus software.','bluetooth':'Have you tried mouthwash?','windows':'Ah, I think I see your problem. What version?','apple':'You do mean the computer kind?','spam':'You should see if your mail client can filter messages.','connection':'Contact Telkom.'}
   
    while (not query=='quit'):
        x=(support.get(str(query)))
        if x is None:
            print('Curious, tell me more.\n',end='')
            query=get_input()
        else:
            print(x)
            query = get_input()    



if __name__=='__main__':
    main()