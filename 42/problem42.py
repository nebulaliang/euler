'''
Problem 42
'''
import math
# check whether given number is triangle number
def isTriangle(num):
    begin = int(math.floor(math.sqrt(num*2)))
    if begin*(begin+1)==num*2:
        return True
    else:
        return False
    
# return the word value for the given word
def wordValue(word):
    value = 0
    for c in word:
        #ord() returns the ASCII value for given character 
        value+=ord(c)-ord('A')+1
    return value

# given filename, return the number of triangle numbers
# read file character by character, split by comma and omit quotes
def numOfTriangle(filename):
    count = 0
    with open(filename) as f:
        word = ''
        while True:
            c = f.read(1)
            if c=='"':     #omit char '"'
                continue
            elif c==',':  #get recent work
                if(isTriangle(wordValue(word))):
                    count+=1
                word=''
            elif not c:   #means end of file
                if(isTriangle(wordValue(word))):
                    count+=1
                break
            else:    #append to recent word
                word+=str(c)
    return count   


if __name__ == '__main__':      
    print numOfTriangle('words.txt')