
from math import *   # bigger prime divisor of an x number
from monotorize import monotorize


@monotorize
def euler1():
    '''sum of all the multiples of 3 or 5 below 1000'''
    return sum([i for i in range(0, 1000, 5) if i % 3 == 0])


@monotorize
def euler1_b():
    '''sum of all the multiples of 3 or 5 below 1000'''
    summ = 0
    for i in range(0, 1000, 5):
        if i % 3 == 0:
            summ += i
    return summ


def euler2():  # fibonaci
    '''
    find the sum of the even-valued terms, 
    whose values do not exceed four million,
    by fibonacci sequence values
    '''
    a, b = 0, 1
    summ = 0
    limit = 4000000
    while b <= 4000000:
        if b % 2 == 0:
            summ += b
        a, b = b, a+b
    return summ


def euler3():
    '''What is the largest prime factor of the number 600851475143 '''
    primes = unpack_primes()
    return primes[-1]


def euler4():  # palindrome
    ''' largest palindrome made from the product of two 3-digit numbers.'''
    max_value = 0
    for n in range(900, 1000):
        for m in range(900, 1000):
            x = str(n*m)
            y = ''.join(reversed(x))
            if x == y:
                max_value = max(max_value, int(x))
    return max_value


def euler5():
    '''
    What is the smallest positive number that is evenly divisible
    by all of the numbers from 1 to 20?What is the smallest positive
    number that is evenly divisible by all of the numbers 
    from 1 to 20?
    '''
    # 2520 tooked from the exercise
    limit = 2520*1000
    for test in range(2520, limit, 2520):
        found = True
        for i in range(11, 21):
            if test % i != 0:
                found = False
                break
        if found:
            return test


def euler6(limit=100):
    '''difference between the sum of the squares of the first one
    hundred natural numbers and the square of the sum.'''
    soma = 0
    square = 0
    for i in range(1, limit):
        soma += i
        square += i**i
    return soma*soma - square


def euler9():  # Pythagorean triplet
    '''Pythagorean triplet for which a + b + c = 1000.'''
    for a in range(1, 500):
        for b in range(1, 500):
            c = 1000-a-b
            if (a*a+b*b) == c*c:
                return a, b, c


def euler16(number):
    '''sum of digits in a number '''
    return sum([int(x) for x in str(number)])


@monotorize
def euler20(n):
    '''sum of factorial recursive'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n*euler20(n-1)


@monotorize
def euler20b(n):  # OPTIMAL
    '''factorial generator'''
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod


def euler21():
    '''sum of all the amicable numbers under 10000.'''
    inpt = int(input('chose number limit '))
    sum_final = 0
    for number in range(1, inpt):
        if amicable_numbers(number):
            sum_final += number
    return sum_final


def euler29(n, m):
    '''two ranges product indexs. no duplicates '''
    lista = set()
    for x in range(2, n+1):
        for i in range(2, m+1):
            lista.add(x**i)
    return lista
