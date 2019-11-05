# JHNLYD001

def wordlist(word):
    d = []
    for i in range(len(word)):
        d.append(word[i])
    d = sorted(d)
    return (d)



print ('***** Anagram Finder *****')
try:
    original_file = open('EnglishWords.txt', 'r')       #appending data from word'START' to end of file to a list
    b = original_file.read()
    a = b.find('START')
    file = b[a::]
    file_list = sorted(file.split())
    yes = 1
except:
    print ('Sorry, could not find file \'EnglishWords.txt\'.')
    yes = 0
    
if yes == 1:
    length = int (input ('Enter word length:\n'))
    print ('Searching...')
    
    len_list = []
        
    for i in range (len(file_list)):
        if len(file_list[i]) == length:
            len_list.append(file_list[i])
        else:
            continue    
    
    file_name = input ('Enter file name:\n')
    print ('Writing results...')
    write2file = open(file_name, 'w')
                
    if len(len_list) > 1:  
        
        temp = []
        checker = []
        
        for i in range (len(len_list)):
            
            if not len_list[i] in checker:
                templist = [len_list[i]]
                checker.append(len_list[i])
                
                for j in range (i, len(len_list)):
                    if len_list[i] != len_list[j]:
                        if wordlist(len_list[i]) == word_to_list(len_list[j]):
                            templist.append(len_list[j])
                            checker.append(len_list[j])
                        else:
                            continue
                    else:
                        continue
            else:
                continue
            
            if (len(templist)) > 1:
                temp.append(templist)
                
    for z in range (len(temp)):
        write2file.write(str(temp[z])+'\n')
        
    write2file.close()