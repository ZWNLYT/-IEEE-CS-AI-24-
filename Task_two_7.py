import re
def count_words(file_path):
    word_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = re.findall(r'\b\w+\b', line.lower())
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
    return word_count
def print_word_count(word_count):
    for word, count in word_count.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    try:
        word_count = count_words(file_path)
        print("Word count:")
        print_word_count(word_count)
    except FileNotFoundError:
        print("File not found.")
