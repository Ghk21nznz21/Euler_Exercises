'''
Some Resolved Euler Exercises from 1 to 30
'''
from basis.AmpleMathClass import AmpleMathFunctions
from basis.AmpleWithinNumberClass import AmpleWithinNumberFunctions


math_holder = AmpleMathFunctions()
within_number_math = AmpleWithinNumberFunctions()


def amicable_numbers(number: int, number2: int) -> bool:
    '''
    check if sum of digits of the first number is
    equal to the second number and vice-versa
    '''
    if number != number2:
        boolean1 = sum(math_holder.get_divisors(number)) == number2
        boolean2 = sum(math_holder.get_divisors(number2)) == number
        if all([boolean1, boolean2]):
            return True
    return False


def euler1(max_number=1000) -> int:
    '''sum of all the multiples of 3 or 5 below 1000'''
    return sum((i for i in range(0, max_number, 5) if i % 3 == 0))


def euler3():
    '''What is the largest prime factor of the number 600851475143 '''
    *_, last = math_holder.generate_primes(600851475143)
    return last


def euler4():
    ''' largest palindrome made from the product of two 3-digit numbers.'''
    max_value = 0
    for n in range(900, 1000):
        for m in range(900, 1000):
            current = n*m
            if current > max_value:
                if within_number_math.is_palindrome(current):
                    max_value = current
    return max_value


def euler5() -> int | float:
    '''
    Smallest number that is divisible
    by all of the numbers from 1 to 20
    '''
    limit = 2520*1000
    for test in range(2520, limit, 2520):
        found = True
        for i in range(11, 21):
            if test % i != 0:
                found = False
                break
        if found:
            return test
    return None


def euler9() -> list[int] | None:
    '''Pythagorean triplet for which a + b + c = 1000.'''
    for a in range(1, 500):
        for b in range(1, 500):
            c = 1000-a-b
            if (a*a+b*b) == c*c:
                return a, b, c
    return None


def euler21(limit: int) -> int:
    ''' sum of all the amicable numbers under some number '''
    return sum((i for i in range(limit) if amicable_numbers(i, limit)))

