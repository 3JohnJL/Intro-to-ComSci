
def latin_to_english(d):
   a = d
   c = len(d)
   b = d[0:(c-2):1]
   e = len(b)
   place = 0
   if b[-1] == "w":
      word = b[0:(e-1):1]
      return (word)
   else:
      for i in range (1, e+1):
         if b[-i] == "a":
            place = i
            break
      word = (b[(-place+1)::1] + b[0:(e-place):1])
      return (word)
                                
def english_to_latin(d):
    a = d
    c = len(d)
    b = 0
    for i in range(c):
        if a[0] == "a" or a[0] == "e" or a[0] == "i" or a[0] == "o" or a[0] == "u":
            break
        else:
            b = b + 1
            a = a[1::1]            
    if b == 0:
        return (d + "way")
    else:
        return (d[b::1] + "a" + d[0:b:1] + "ay")
        
def to_pig_latin(sentence):
    num_of_words = sentence.count(" ") + 1
    words = sentence.split()
    new_words = []
    for i in range (num_of_words):
        word_in_edit = words[i]
        changed_word = english_to_latin(word_in_edit)
        new_words.append(changed_word)
    aa = (" ".join(new_words))
    return (aa)
    
def to_english(sentence):
    word_count = sentence.count(" ") + 1
    word_list = sentence.split()
    new_list = []
    for j in range (word_count):
        edit_word = word_list[j]
        edited_word = latin_to_english(edit_word)
        new_list.append(edited_word)
    bb = (" ".join(new_list))
    return (bb)