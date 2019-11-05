#Lydia John

def print_square():             #prints out a 5x5 square
    print ("*****")
    print ("*   *")
    print ("*   *")
    print ("*   *")
    print ("*****")

def print_rectangle(w, l):
    print ("*"*w)                                       #prints out a rectangle according to user specified width and height
    for i in range (l-2):
        print ("*", " "*(w-2), "*", sep="")
    print ("*"*w)
    
def get_rectangle(w, l):
    return str("*"*w + "\n" + ("*" + " "*(w-2) + "*" + "\n")*(l-2) + "*"*w)