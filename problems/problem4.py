"""
Largest palindrome product

Problem 4
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isPalindrome(product):
    """
    test if it is a palindrome
    """
    return str(product) == str(product)[::-1]



def largest_palindrome(digits):
    """
    takes the number of digits and finds the largest palindrome made
    based on the products of n digits
    """
    largest = 0 #remember the largest palindrome
    #I'm setting up the ranges this for convenience
    maxa = int('9'*digits)
    mina = int('1'+'0'*(digits-1))-1
    maxb = int('9'*digits)
    minb = int('1'+'0'*(digits-1))-1

    for a in xrange(maxa, mina, -1): #started from the top now we here
        for b in xrange(maxb, minb, -1):
            product = a * b
            if product < largest: break #if the current product is less than the largest we can break
            if isPalindrome(product):
                if product > largest:
                    largest = product
                    print "{0}x{1}=={2}".format(a,b,product)
                    break #we can break once we find the largest palindrome per nested iteration
    print str(largest) + "\n"


largest_palindrome(2)
largest_palindrome(3)
