total_sum = 0
while True:
    user_input = input("Enter a number: ")
    number = int(user_input)
    if number == 0:
        break
    total_sum += number

print(f"The final sum is: {total_sum}")