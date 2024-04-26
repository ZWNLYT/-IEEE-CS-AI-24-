def is_palindrome(word):
    word = word.lower()

    return word == word[::-1]

def main():
    try:
        word = input("Enter a word: ")
        if is_palindrome(word):
            print(f"The word '{word}' is a palindrome.")
        else:
            print(f"The word '{word}' is not a palindrome.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()