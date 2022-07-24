import math
"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number * number for number in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"



def is_prime(number):
    if number > 1:  #if i == 0 or i == 1: continue
        for i in range(2,number):
            if number % i == 0:
                return False
    else:
        return False
    return True



    # prime_list = []
    # for i in number_list:
    #     if i == 0 or i == 1:
    #         continue
    #     else:
    #         for j in range(2, int(i / 2) + 1):
    #             if i % j == 0:
    #                 break
    #         else:
    #             prime_list.append(i)
    # return prime_list


def filter_numbers(number_list, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        return list(filter(lambda x: x % 2 != 0, number_list))
    # if "even" in filter_type:
    if filter_type == EVEN:
        return list(filter(lambda x: x % 2 == 0, number_list))
    if filter_type == PRIME:
        #return list(map(is_prime, number_list))
        return list(filter(is_prime, number_list))





    #   return list(filter(lambda x: x % 2 != 0, number_list))
    #return list(filter(lambda x: x % 2 != 0, number_list))

    #if filter_type == ODD:
    #   return [number for number in number_list if number % 2 !=0]


    #return list(filter(lambda x: x % 2 == 0, number_list))

    #if filter_type == EVEN:
    #   return [number for number in number_list if number %2 == 0]
    #if filter_type == PRIME:

    #   return [x for x in number_list if all(x % y != 0 for y in range(2, int(math.sqrt(x + 1))))] #- ?random number of errors on test from 0 - 5? problem with 0,1 mby add manual?

    #   return [number for number in number_list if 0 not in [number % i for i in range(2, int(number/2)+1)]] #1 error problem with 0,1 mby add
    # is_prime = lambda n: all( n%i != 0 for i in range(2, int(n**.5)+1) )

    # def primes_method3(n):
    #   n = numbers_list
    #   out = list()
    #  for num in range(1, n+1):
    #     if all(num % i != 0 for i in range(2, int(num**.5 ) + 1)):
    #            out.append(num)
    #   return out
    # def prime(number):

    #     for i in range(2, number):
    #         if number_list % i == 0:
    #             return False
    #
    #     return True
    #
    # prime_list=list(map(prime, number_list))

    # if number == 0 or number == 1:
    #     return False
    # for i in range(2, int(number // 2) + 1):
    #     if number % i == 0:
    #         return False
    #     else:
    #         return True

    # return list(map(int(prime,number_list)))

    # primes = []
    # for number in number_list:
    #    if all(number % i != 0 for i in range(2, int(number ** .5) + 1)):
    #        primes.append(number)

    # for number in number_list:
    #   if all(number%i!=0 for i in range(2,int(math.sqrt(number))+1)):
    #       primes.append(number)
    # return primes