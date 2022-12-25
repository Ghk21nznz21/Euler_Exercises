
class AmpleWithinNumberFunctions:
    '''
    Holds Functions that allow to check interesting characteristics
    within the number itself
    '''

    @staticmethod
    def circle_number(number: int) -> bool:
        ''' list of all the circular number of the number '''
        string = str(number)
        circle = [int(string[i:] + string[:i]) for i in range(len(string))]
        return circle

    def is_padigital(self, number: int) -> bool:
        ''' check if number dosent have repeated numbers'''
        lista = list(self.get_digits(number))
        if len(lista) == len(set(lista)):
            return True
        return False

    @staticmethod
    def is_palindrome(number: int) -> bool:
        ''' check if the number is equal to its reverse'''
        number = str(number)
        return number == ''.join(reversed(number))

    @staticmethod
    def get_digits(number: int) -> bool:
        ''' split the number by digits'''
        return (int(x) for x in str(number))
