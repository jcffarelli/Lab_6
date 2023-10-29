# Create main function
def main():
    end = True
    while end:
        # Create menu
        print("Menu")
        print("-" * 13)
        print("1. Encode\n2. Decode\n3. Quit\n")
        option = int(input('Please enter an option: '))
        if option == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!\n")
            store = encode(password)
        elif option == 2:
            # Show user previously encoded and now decoded string
            print(f"The encoded password is {store}, and the original password is {decode(store)}.")
        elif option == 3:
            end = False


# Create function to encode
def encode(password):
    code = str()
    for i in password:
        new = int(i)
        if new > 6:
            code += str(new - 7)
        else:
            code += str(new + 3)

    return code


# Create decode function
def decode(password):
    decoded = ""
    for i in password:
        # Subtracts 3 from each character in encoded password
        n = int(i) - 3
        # If n goes negative after subtraction number wraps around
        if n < 0:
            decoded += str(n + 10)
        # If n is positive it is just added to the decoded string
        else:
            decoded += str(n)
    return decoded


if __name__ == "__main__":
    main()
