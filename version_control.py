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
            # edit option 2 to fit your code, just used pass as placeholder
            pass
        elif option == 3:
            end = False

# Create function to encode
def encode(password):
    code = str()
    for i in password:
        new = int(i)
        code += str(new + 3)
    return code


if __name__ == "__main__":
    main()
