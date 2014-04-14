'''
Problem 14
'''

# global variable, used to store the computed key value pairs 
# represent start number and numbers of terms of the chain 
cache={1:1}

# given start number, return the number of terms of the chain
# recursively build cache if given start number not exists in cache
def numOfChain(n):
    if not cache.has_key(n):
        if n%2==0:
            cache[n] = 1+numOfChain(n/2)
        else:
            cache[n] = 1+numOfChain(3*n+1)
    return cache[n]        

# given the bound number, print out the longest chain number
def longestChain(bound):
    start_num = 0
    cur_longest = 0
    for i in xrange(1,bound):
        chain = numOfChain(i)
        if chain>cur_longest:
            cur_longest = chain
            start_num = i
    print "the starting number %s produces the longest chain which contain %s terms" %(start_num,cur_longest)

if __name__ == '__main__':
    longestChain(1000000)