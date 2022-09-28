"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError
    list = []
    number = 2
    while len(list) < number_of_primes:
        if is_prime(number):
            list.append(number)
        number += 1
    return list


def is_prime(number):
    for i in range(2, number): #find if a factor exists other than 1 and itself
        if (number % i) == 0:
            return False
    return True
