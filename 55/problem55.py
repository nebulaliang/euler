'''
Problem 55
'''
# reverse given integer
# e.g. reverseInt(123) will be 321
def reverseInt(num):
    return int(str(num)[::-1])

# check whether given number is Palindromic
# e.g. :
# isPalindromic(123)   ->  False
# isPalindromic(121)   ->  True
def isPalindromic(num):
    if num==reverseInt(num):
        return True
    else:
        return False
#check whether given number is Lychrel number in given iteration times 
#NOTE: The problem only require iterations of 50. However, for further potential using,
#      we would let it be parameterized 
def isLychrel(num, iteration_times):
    for i in range(iteration_times):
        num = num+reverseInt(num)
        if isPalindromic(num):
            return False
    return True

# get the count of Lychrel numbers below given bound number and given iteration times
def numOfLychrel(bound,iteration_times):
    count = 0
    for i in range(1,bound):
        if isLychrel(i,iteration_times):
            count+=1
    return count
            

if __name__ == '__main__':
    print numOfLychrel(10000,50)
