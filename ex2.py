def right(row):
    """Print right-aligned pattern."""
    for i in range(1, row + 1):
        print("*" * i)

def para(row):
    """Print pyramid pattern."""
    for i in range(1, row + 1):
        print(" " * (row - i) + "*" * (2 * i - 1))

def lef(row):
    """Print left-aligned pattern."""
    for i in range(1, row + 1):
        print(" " * (row - i) + "*" * i)

def num(start, end):
    """Analyze the numbers in a range, check if they are odd or even, and print their sum."""
    total = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(f"Number {num} is even")
        else:
            print(f"Number {num} is odd")
        total += num
    print(f"Sum of all numbers from {start} to {end} is: {total}")

def main():
    while True:
        print("\nWelcome to the pattern generator")
        print("\nSelect an option: ")
        print("1. Right")
        print("2. Para")
        print("3. Left")
        print("4. Analyze a range of numbers")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue

        if choice in [1, 2, 3]:
            try:
                row = int(input("Enter the number of rows for the pattern: "))
                if row <= 0:
                    print("Row count must be positive!")
                    continue  # Prompt the user again if the row count is not valid
            except ValueError:
                print("Invalid input for rows. Please enter a valid number.")
                continue  # Prompt the user again if the input is invalid

            if choice == 1:
                right(row)
            elif choice == 2:
                para(row)
            elif choice == 3:
                lef(row)

            print("\n" + "-" * 80)

        elif choice == 4:
            try:
                start = int(input("Enter the start of the range: "))
                end = int(input("Enter the end of the range: "))
                if end < start:
                    print("End range must be greater than start!")
                    continue  # Ask for input again if the range is invalid
            except ValueError:
                print("Invalid range. Please enter valid numbers.")
                continue  # Ask for input again if the input is invalid

            num(start, end)

        elif choice == 5:
            print("Exiting the program.")
            break  # Exit the loop and end the program

        else:
            print("Invalid choice. Please select a valid option (1-5).")

# Run the program
main()