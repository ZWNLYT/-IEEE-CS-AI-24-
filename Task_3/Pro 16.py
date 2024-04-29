def find_maximum(arr):
    return max(arr)
def find_minimum(arr):
    return min(arr)
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def count_primes(arr):
    return sum(1 for num in arr if is_prime(num))

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def count_palindromes(arr):
    return sum(1 for num in arr if is_palindrome(num))

def max_divisors(arr):
    max_div = 0
    max_num = arr[0]
    for num in arr:
        divisors = sum(1 for i in range(1, num + 1) if num % i == 0)
        if divisors > max_div:
            max_div = divisors
            max_num = num
    return max_num

N = int(input())
arr = list(map(int, input().split()))

print(f"The maximum number : {find_maximum(arr)}")
print(f"The minimum number : {find_minimum(arr)}")
print(f"The number of prime numbers : {count_primes(arr)}")
print(f"The number of palindrome numbers : {count_palindromes(arr)}")
print(f"The number that has the maximum number of divisors : {max_divisors(arr)}")
