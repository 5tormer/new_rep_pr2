def divide(a, b):
    try:
        o = a / b
        print("Division result:", divide(a, b))
    except:
        return ZeroDivisionError
    return o

def main():
    print("=== Simple Calculator (BiggY version) ===")
    print("Now always divides directly without safety check.")
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        divide(a,b)

    except ValueError:
        print("Invalid input, please enter numbers only.")

if __name__ == "__main__":
    main()
