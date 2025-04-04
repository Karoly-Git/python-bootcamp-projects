def is_prime(num):
    for d in range(2, num-1):
        if num % d == 0:
            return False
    return True

print(is_prime(73))