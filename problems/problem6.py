"""
Sum square difference

Problem 6

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

def sum_of_squares_diff(first_natural):
    total_sum_of_sqrs = sum_of_sqrs(first_natural)
    total_sqr_of_sums = sqr_of_sums(first_natural)
    print "Sum of Squares: {0}".format(total_sum_of_sqrs)
    print "Square of Sums: {0}".format(total_sqr_of_sums)
    print "Difference is {0}".format(total_sqr_of_sums-total_sum_of_sqrs)
    print ""

def sum_of_sqrs(first_natural):
    return sum([x**2 for x in xrange(1, first_natural+1)])

def sqr_of_sums(first_natural):
    return ((first_natural*(first_natural+1))/2)**2

sum_of_squares_diff(10)
sum_of_squares_diff(100)
