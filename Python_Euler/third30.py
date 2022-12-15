from euler_exs_2nd10 import euler20 as factorial
from prime_generator import prime_gen2


def five_conc():
    inpt = int(input('number '))
    lista = [3, 7, 109, 673]
    for prime in prime_gen2(inpt):
        if prime not in lista:
            for index in lista:
                string = str(prime) + str(index)
                string2 = str(index)+str(prime)
                if int(string) in prime_gen2(inpt) and int(string2) in prime_gen2(inpt):
                    if index == lista[-1]:
                        return sum(lista) + prime
                else:
                    break

def euler63():
    summ = 0
    ints = [i for i in range(1, 22)]
    powers = ints
    for i in ints:
        for p in powers:
            numb = i**p
            if len(str(numb)) == p:
                summ += 1
    return summ


def fact_numb(numb):
    lista = [int(x) for x in str(numb)]
    after_numb = 0
    for i in lista:
        after_numb += factorial(i)
    return after_numb


def fact_chain(after_numb):
    lista = [after_numb]
    a = fact_numb(lista[-1])
    while a not in lista:
        lista.append(a)
        a = fact_numb(lista[-1])
    if len(lista) == 60:
        return 1
    else:
        return 0


def euler74_loop():
    soma = 0
    for i in range(2, 1000000):
        soma += fact_chain(i)
    return soma


if __name__ == "__main__":
    print(euler74_loop())


if __name__ == "__main__":
    print(five_conc())

    print(euler63())
