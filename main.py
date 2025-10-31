def divide(a, b):
    return a / b

def main():
    print("=== Simple Calculator (Biggy version) ===")
    print("Now always divides directly without safety check.")
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Division result:", divide(a, b))
    except ValueError:
        print("Invalid input, please enter numbers only.")

if __name__ == "__main__":
    main()
