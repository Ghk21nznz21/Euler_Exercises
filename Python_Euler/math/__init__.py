from monotorize import monotorize



def prime_gen(limit):
    ''' yield prime numbers '''
    for i in range(2, limit):
        prime = True
        max_j = int(pow(i, 0.5)) + 1
        for j in range(2, max_j):
            if i % j == 0:
                prime = False
                break
        if prime:
            yield i


def prime_optimal(limit):
    ''' Prime number can divide any other, except other primes '''
    primes = [2]
    for number in range(3, limit):
        max_divisor = y = int(pow(number, 0.5))+1
        is_prime = True
        for prime in primes:
            if number > max_divisor:
                break
            elif number % prime:
                is_prime = False
        if is_prime:
            primes.append(prime)
    return primes


def unpack_prime_gen():
    ''' unpack prime generators'''
    inpt = int(input("Enter a int number "))
    return [s for s in prime_gen2(inpt)]


def fibo(limit):
    a, b = 0, 1
    index = 0
    while index <= limit:
        yield (a, index)  # pair of tuples (a, index) to get a by index
        a, b = b, a+b
        index += 1


def divisors(number):
    summ = 0
    for i in range(1, number/2):
        if number % i == 0:
            summ += i
    return summ


def amicable_numbers(number):
    summ = divisors(number)
    if divisors(summ) == number and summ != number:
        return True
    else:
        return False


def circle_number(number):  # list of all the circular number of the number
    string = str(number)
    circle = [int(string[i:] + string[:i]) for i in range(len(string))]
    return circle


def is_padigital(number):  # euler41
    lista = [int(x) for x in str(number)]
    if len(lista) == len(set(lista)):
        return True
    else:
        return False
