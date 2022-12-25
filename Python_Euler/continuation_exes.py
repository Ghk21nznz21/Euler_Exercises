from basis.AmpleMathClass import AmpleMathFunctions
from basis.AmpleWithinNumberClass import AmpleWithinNumberFunctions


math_holder = AmpleMathFunctions()
within_number_math = AmpleWithinNumberFunctions()


def euler35(limit: int) -> int:
    ''' circular primes that are below one million'''
    return sum(filter(
        within_number_math.circle_number, math_holder.generate_primes(limit)
        ))


def euler41(limit: int) -> int:
    '''What is the largest n-digit pandigital prime that exists?'''
    for number in reversed(list(math_holder.generate_primes(limit))):
        if within_number_math.is_padigital(number):
            return number
    return None


def euler43():
    '''sum of all 0 to 9 pandigital numbers with this property'''
    first_primes = [2, 3, 5, 7, 11, 13, 17]
    summ = 0
    for number in range(1_000_000_000, 10_000_000_000):
        if within_number_math.is_padigital(number):
            string = str(number)
            rule = []
            for i in range(1, 8):
                rule.append(int(string[i:i+3]) % first_primes[i] == 0)
            if all(rule):
                summ += number
    return summ


def euler44(limit: int) -> int:
    '''
    Find the pair of pentagonal numbers, Pj and Pk, for which their
    sum and difference are pentagonal and D = |Pk − Pj|
    is minimised
    '''
    lista = [x*(3*x - 1)/2 for x in range(1, limit)]
    for j in lista:
        for k in lista:
            if (j+k) in lista and abs(k-j) in lista:
                yield abs(k-j)


def euler56(limit: int) -> int:
    '''
    Find maximum digital sum of the exponential
    of two numbers samller then (100)
    '''

    maxx = 0
    for a in range(1, limit):
        for b in range(1, limit):
            n = sum(within_number_math.get_digits(a**b))
            if n > maxx:
                maxx = n
    return maxx


def fact_numb(numb: int) -> int:
    '''
    :param: number
    :return:  summ of the factorial of all the digits
    '''
    summ = 0
    for i in within_number_math.get_digits(numb):
        summ += math_holder.factorial(i)
    return summ
