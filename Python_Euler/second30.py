from math import *
from first30 import euler20b, euler6

def euler34():
    '''sum of all numbers which are equal to the sum of the factorial of their digits.'''
    summ= 0
    for number in range (1, 2540160):
        lista=[ euler20b(int(digit)) for digit in str(number) ]
        if sum(lista)== i:
            summ += number
    return summ


def euler35():
    ''' circular primes that are below one million'''
    lista= prime_optimal(1000000)
    summ= 0
    for number in lista:
        circle_list=circle_number(number)
        prime=True
        for circle in circle_list:
            if circle not in lista:
                prime=False
                break
        if prime:
            summ+=1
    return summ 


def euler41():
    '''What is the largest n-digit pandigital prime that exists?'''
    for number in reversed(prime_optimal(1000000000)): #10 digit number
        if is_padigital(number):
          return number
        

def euler43():
    '''sum of all 0 to 9 pandigital numbers with this property'''
    summ=0
    for number in range(1000000000, 9999999999):    #10digits
        divisions_list=[2,3,5,7,11,13,17]
        if is_padigital(number):
            string= str(numb)
            list_div= [ int(string[a:a+3]) for a in range(1,8) ]
            rule_verified=True
            for i in range(7):
                if divisions_list[i]%int(string[i+1:i+3]) !=0:
                    rule_verified=False
            if rule_verified:
                summ+= number 
    return summ


def euler44(): #pentagon_number
    ''' 
    Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are 
    pentagonal and D = |Pk − Pj| is minimised; what is the value of D?
    '''
    inpt= int( input( 'number ' ))
    lista= [x*(3*x -1)/2 for x in range (1, inpt)]
    lista_f=[]
    for j in lista:
        for k in lista:
            if (j+k) in lista and abs(k-j) in lista:
                lista_f.append(abs(k-j))
    return lista_f


def euler48(): 
    '''last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000'''
    inpt= int(input('Limit number ' ))
    out= str(euler6(inpt))
    joiner= out[-10:]
    return int(''.join([ "%d"%x for x in joiner])) 


def euler53(n): 
    ''' how many combinations 1<n<100 are >1 000 000'''
    summ=0
    for n in range(9,101):
        inner_sum=0
        for r in range(1,n):
            result= fact(n)/( fact(r)*fact(n-r) )
            if result >1000000:
                inner_sum +=1
        summ +=inner_sum
    return summ


def euler56():
    '''Considering natural numbers of the form, a**b, where a, b < 100, what is the maximum digital sum?'''
    maxx= 0
    for a in range(1,100):
        for b in range(1,100):
            string=str(a**b)
            summ= sum(int(x) for x in string)
            if summ > maxx:
                maxx= summ
    return maxx