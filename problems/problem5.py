"""
Smallest multiple

Problem 5
2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""


#### Brute force method
def isDivisable(xNum, yList):
    for y in yList:
        if xNum%y != 0:
            return False
    return True

def smallest_multiple(top_range):
    """
    takes top range to make a list from 1 to n
    will return the smallest number which is multiple by all numbers in the list

    No need to check 1 as everything will be divisable. So 2 onwards
    """
    list = [x for x in range(2,top_range)]
    base = 0

    while True:
        base += 1
        if isDivisable(base, list) == True:
            return base
        else:
            print "Current iteration of {0}".format(base)

print smallest_multiple(10)
#print smallest_multiple(20)
#Takes too long for 1-20.


#nicer method
#http://codereview.stackexchange.com/questions/67938/project-euler-5-lowest-multiple-of-1-through-20
def lowest_common_multiple(nfrom, nto):
    lcm = nfrom
    for i in range(nfrom, nto+1):
        sum = lcm
        print "sum is {0}, iteration is {1}".format(sum, i),
        while (sum % i != 0):
            print " adding {0}".format(lcm),
            sum += lcm
        print ""
        lcm = sum
    return lcm

print lowest_common_multiple(1,20)
