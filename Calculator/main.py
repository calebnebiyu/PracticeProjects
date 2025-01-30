from art import logo
print(logo)

def calculator():
    first_num = float(input("What's the first number? "))

    def add(n1, n2):
        return n1 + n2

    def subtract(n1, n2):
        return n1 - n2

    def multiply(n1, n2):
        return n1 * n2

    def divide(n1, n2):
        return n1 / n2

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    calculation = True
    while calculation:

        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation: ")
        # if operation not in operations:
        #     operation = 0
        second_num = float(input("What's the next number? "))
        answer = operations[operation](first_num, second_num)

        print(f"{first_num} {operation} {second_num} = {answer}")
        continue_calculating = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if continue_calculating == "y":
            first_num = answer
            calculation = True
        elif continue_calculating == "n":
            calculation = False
            stop = input("Would you like to stop the calculation? (y/n): ")
            if stop == "n":
                print("\n" * 20)
                calculator()
            elif stop == "y":
                print(f"{answer} is your final answer.")
            else:
                print("You did not enter a valid option. The calculation will stop.")
calculator()