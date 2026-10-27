"""Simple command-line calculator."""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


OPERATIONS = {
    "1": ("Add", add),
    "2": ("Subtract", subtract),
    "3": ("Multiply", multiply),
    "4": ("Divide", divide),
}


def read_number(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Please enter a valid number.")


def main() -> None:
    print("Calculator")
    print("-" * 20)

    while True:
        print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "5":
            print("Goodbye.")
            break

        if choice not in OPERATIONS:
            print("Invalid option. Try again.")
            continue

        a = read_number("First number: ")
        b = read_number("Second number: ")
        name, func = OPERATIONS[choice]

        try:
            result = func(a, b)
        except ZeroDivisionError as exc:
            print(exc)
        else:
            print(f"{name} result: {result}")


if __name__ == "__main__":
    main()
