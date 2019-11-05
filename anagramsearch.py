#JHNLYD001
print ('***** Anagram Finder *****')


try:
    myfile = open('EnglishWords.txt', 'r')
    b = myfile.read()
    a = b.find('START')                             #append all data from word 'START' to the end of the file to a list
    file = b[a::]
    filelist = sorted(file.split())
    yes = 1
except:
    print ('Sorry, could not find file \'EnglishWords.txt\'.')          #if cannot find file
    yes = 0 

if yes == 1:
    word = input ('Enter a word: ')                 #user inputs word to find anagram for
    word = word.lower()    
    
    anagrams = []
    
    for i in range (len(filelist)):         
        if len(word) == len(filelist[i]):            # if len of word is equal to words from list, word list is created
            word_lett = []
            file_lett = []
            for j in range (len(word)):
                word_lett.append(word[j])
            for k in range (len(filelist[i])):
                file_lett.append(filelist[i][k])
            if sorted(word_lett) == sorted(file_lett):
                anagrams.append(filelist[i])
            else:
                continue
        else:
            continue
        
    if len(anagrams) >= 1:
        if word in anagrams:
            anagrams.remove(word)   
    
    if len(anagrams) == 0:
        print ('\nSorry, anagrams of \'' + word + '\' could not be found.')
    else:
        print ('\n'+ str(anagrams))