def is_prime(n):
    
    divider = 2
    
    if(n == 1):
        return False

    while (n % divider != 0):
        divider += 1

    if(divider == n):
        return True
    else:
        return False    

def find_biggest_prime(n):
    primes = list()
    
    for iteration in range(2, n + 1):
        if(is_prime(iteration)):
            primes.append(iteration)
    
    if(len(primes)):
        return max(primes)
    else:
        return None

# number = int(input("Enter a value: "))
# result = find_biggest_prime(number)
# print(result)