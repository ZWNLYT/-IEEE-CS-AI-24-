def p_d():
    data = input("Enter a list of values (separated by commas): ")
    data = [int(x) for x in data.split(",")]
    total_values = len(data)
    freq = {}
    for value in data:
        if value in freq:
            freq[value] += 1
        else:
            freq[value] = 1
    prob = {}
    for value, frequ in freq.items():
        prob[value] = frequ / total_values
    return prob
print(p_d())

