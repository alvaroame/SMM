# This function is to compute if a number is prime
def is_prime(num, div=2):
    if num == div:
        return True
    elif num % div == 0:
        return False
    elif num == 1:
        return False
    else:
        return is_prime(num, div + 1)


# This function is to get a list of numbers and for every number is computed if it is prime, in that case,
# the number is added to a list of primes
# return:
# numbers: list of numbers from 1 to n
# primes: list of numbers primes from 1 to n
def get_data(x):
    numbers = []
    primes = []
    for i in range(1, x + 1):
        numbers.append(i)
        if is_prime(i):
            primes.append(i)
    return numbers, primes


# This function is to compute the LCM (The Least common multiple) from a list of numbers
# It uses the division method, basically divided every number from the least by primes until all are ones
def get_mcm(numbers, primes):
    mcm = 1
    index_prime = 0
    while index_prime < len(primes):
        prime = primes[index_prime]
        next_prime = True
        for index in range(len(numbers)):
            if numbers[index] % prime == 0:
                numbers[index] = int(numbers[index] / prime)
                next_prime = False
        if next_prime:
            index_prime += 1
        else:
            mcm *= prime
    return mcm


x = 20
numbers, primes = get_data(x)
mcm = get_mcm(numbers, primes)
print(mcm)
