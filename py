total = 0

while True:
    try:
        num_str = input("Enter a number (or -1 to exit): ")
        num = int(num_str)

        if num == -1:
            break

        total += num
    except ValueError:
        print("Invalid input. Please enter a valid number or -1 to exit.")

print(f"Sum of all numbers entered: {total}")
