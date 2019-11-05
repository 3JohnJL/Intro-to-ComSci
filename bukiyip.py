#Lydia John

def bukiyip_to_decimal(a):
    num = "{0:0>3}".format(str(a))
    nines = int(num[0])
    threes = int(num[1])
    end = int(num[2])
    val = (9*nines) + (3*threes) + (1*end)
    return (end)

def decimal_to_bukiyip(a):
    number = a    
    nines = 0
    threes = 0
    while number >= 9:
         nines = nines + 1
         number = number - 9
    else:
        while number >= 3:
            threes = threes + 1
            number = number - 3
    phrase = (str(nines) + str(threes) + str(number))
    if phrase[0] == "0":
        if phrase[1] == "0":
            return (str(number))
        else:
            return (str(threes) + str(number))
    else:
        return (str(nines) + str(threes) + str(number))
        
def bukiyip_add(a, b):
    dec_a = bukiyip_to_decimal(a)
    dec_b = bukiyip_to_decimal(b)
    val = dec_a + dec_b
    val = decimal_to_bukiyip(val)
    return (val)
    
def bukiyip_multiply(a, b):
    dec_a = bukiyip_to_decimal(a)
    dec_b = bukiyip_to_decimal(b)
    val = dec_a * dec_b
    val = decimal_to_bukiyip(val)
    return (val)