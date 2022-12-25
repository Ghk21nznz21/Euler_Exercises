from collections.abc import Generator


class AmpleMathFunctions:
    '''
    Saves Very Usefull Functions
    Commonly Used
    '''

    @staticmethod
    def generate_primes(limit: int) -> Generator[int]:
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

    @staticmethod
    def get_divisors(number: int) -> Generator[int]:
        ''' get the numbers that fully divide that number'''
        for i in range(1, number//2):
            if number % i == 0:
                yield i

    @staticmethod
    def fibonaci(size: int) -> Generator[int]:
        ''' get the fibonaci numbers'''
        a, b = 0, 1
        for _ in range(size):
            a, b = b, a+b
            yield a
        yield b

    def factorial(self, number: int) -> int:
        ''' get the factorial of that number, with recursive '''
        if number == 1:
            return number
        return number*self.factorial(number-1)
