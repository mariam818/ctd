numbers = []

while True:
    user_input = input("Enter a number ('q' to quit): ")
    
    if user_input == 'q':
        break
    numbers.append(int(user_input))


if numbers:
    print("Largest number:", max(numbers))
    print("Smallest number:", min(numbers))

