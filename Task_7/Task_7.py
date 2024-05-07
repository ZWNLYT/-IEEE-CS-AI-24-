def calculate_statistics():
    count = input("Enter the count array (comma-separated integers): ")
    count = list(map(int, count.split(',')))
    total_elements = sum(count)

    minimum = min(i for i, c in enumerate(count) if c > 0)
    maximum = max(i for i, c in enumerate(count) if c > 0)
    mean = sum(i * c for i, c in enumerate(count)) / total_elements

    elements = sorted(i for i, c in enumerate(count) for _ in range(c))
    median = elements[total_elements // 2] if total_elements % 2 else (elements[total_elements // 2 - 1] + elements[total_elements // 2]) / 2

    mode = max(range(256), key=count.__getitem__)

    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Mean:", mean)
    print("Median:", median)
    print("Mode:", mode)

calculate_statistics()