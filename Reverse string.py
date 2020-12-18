# palindrome - is a word or phrase which reads the same backward or normal. For example: madam, nurse run...

while True:   # infinity loop
    string = input("Please enter a phrase to check whether it is palindrome: ")

    reverse = string[::-1]
    print("Reverse phrase:")
    print(reverse)

    if reverse == string:
        print("The phrase is a palindrome")
    else:
        print("The phrase is not a palindrome")