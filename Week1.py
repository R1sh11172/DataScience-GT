#Introductory python lesson w/ all lessons nn

def cube(n): 
    return n * n * n
    raise NotImplementedError("Did not implement the cube function")

def factorial(n):
    result = 1
    for i in range (n): 
        result = result * (i + 1); 
    return result
    raise NotImplementedError("Did not implement factorial function")

def count_digits(n):
    digisum = 0
    s = str(n)
    for letter in s: 
        digiSum += 1
    return digiSum
    raise NotImplementedError("Did not implement the count_digits function")

def average_grade(scores, targetGrade): 
    finalScore = (len(scores) + 1) * targetGrade
    for i in scores: 
        finalScore -= scores[i]
    return finalScore
    raise NotImplementedError("Did not implement the average_grade function")

def slice_product(numList, start_pos, end_pos): 
    result = 1
    for i in range (start_pos, end_pos + 1): 
        result *= numList[i]

    return result
    raise NotImplementedError("Did not implement slice_product function")

def encrypt(message, shift): 
    str = message
    numChar = len(message)
    chars = []
    overlap = shift % 26

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(numChar): 
        if str[i] != " ": 
            if str[i].islower():
                index = alphabet.index(message[i])
                index += overlap
                chars.append[alphabet[alphabet.index(a[i])]]
            else: 
                temp = message[i].lower()
                index = alphabet.index(temp)
                index -= overlap
                chars.append(alphabet[index].upper())
        else:
            chars.append(" ")

    result = ""
    for i in range (len(chars)): 
        result += chars[i]
    return final
    raise NotImplementedError("Did not implement encrypt function")

def decrypt(message, shift): 
    a = message
    x = len(a)
    chars = []
    offset = shift
    offset = offset % 26
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in range(x):
        if a[i] != " ":
            if a[i].islower():
                index = alphabet.index(a[i])
                index -= offset
                chars.append(alphabet[index])
            else:
                temp = a[i].lower()
                index = alphabet.index(temp)
                index -= offset
                chars.append(alphabet[index].upper())
        else:
            chars.append(" ")
    final = ""

    for i in range (len(chars)):
        final += chars[i]
    return final
    raise NotImplementedError("Did not implement decrypt function")

       

