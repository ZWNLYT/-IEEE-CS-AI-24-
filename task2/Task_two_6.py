def get_numeric_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            numeric_value = float(user_input)
            return numeric_value
        except ValueError:
            print("Please enter a numeric value.")

if __name__ == "__main__":
    prompt = "Please enter a number: "
    numeric_value = get_numeric_input(prompt)
    print("You entered:", numeric_value)
