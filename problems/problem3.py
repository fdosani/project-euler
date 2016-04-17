"""
Largest prime factor

Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
def prime_factor(number):
    base = number
    current = 2 #start with 2
    #loop until the base number is == to the current factor
    while base > current:
        if base % current == 0:
            print "base number: {0}, current factor: {1}".format(base, current)
            base = base/current
        else:
            current += 1
    print "largest prime factor of {0} is: {1}".format(number, current)


prime_factor(13195)
prime_factor(600851475143)
