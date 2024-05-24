def check_prime(num):  
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                return False
        return True
    return False

range_start = int(input("Enter the start of the range: "))
range_end = int(input("Enter the end of the range: "))

prime_numbers = [num for num in range(range_start, range_end+1) if check_prime(num)]
prime_numbers.sort()

print("Prime numbers in the range from", range_start, "to", range_end, "are:")



print(prime_numbers)