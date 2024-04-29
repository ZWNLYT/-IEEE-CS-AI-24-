def get_numbers():
    while True:
        numbers_str = input("Enter a list of numbers separated by commas: ")
        try:
            numbers = [int(num.strip()) for num in numbers_str.split(",")]
            return numbers
        except ValueError:
            print("Invalid input. Please enter a list of integers separated by commas.")

def find_min(numbers):
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value

def find_max(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value
def find_mean(numbers):
    if len(numbers) == 0:
        raise ValueError("Cannot compute mean with an empty list.")
    return sum(numbers) / len(numbers)
def find_mode(numbers):
    from collections import Counter
    counter = Counter(numbers)
    max_count = max(counter.values())
    modes = [num for num, count in counter.items() if count == max_count]
    return modes
def find_median(numbers):
    numbers.sort()
    length = len(numbers)
    if length % 2 == 0:
        median = (numbers[length // 2 - 1] + numbers[length // 2]) / 2
    else:
        median = numbers[length // 2]
    return median

def find_range(numbers):
    return find_max(numbers) - find_min(numbers)

def find_variance(numbers):
    mean = find_mean(numbers)
    variance = sum((num - mean) ** 2 for num in numbers) / len(numbers)
    return variance

def find_STD(numbers):
    return find_variance(numbers) ** 0.5

def find_Quartiles(numbers):
    numbers.sort()
    Q1 = find_median(numbers[:len(numbers) // 2])
    Q3 = find_median(numbers[len(numbers) // 2:])
    return (Q1, find_median(numbers), Q3)

def find_IQR(numbers):
    quartiles = find_Quartiles(numbers)
    return quartiles[2] - quartiles[0]

if __name__ == "__main__":
    numbers = get_numbers()
    print("Min:", find_min(numbers))
    print("Max:", find_max(numbers))
    print("Mean:", find_mean(numbers))
    print("Mode:", find_mode(numbers))
    print("Median:", find_median(numbers))
    print("Range:", find_range(numbers))
    print("Variance:", find_variance(numbers))
    print("Standard Deviation:", find_STD(numbers))
    print("Quartiles:", find_Quartiles(numbers))
    print("Interquartile Range (IQR):", find_IQR(numbers))