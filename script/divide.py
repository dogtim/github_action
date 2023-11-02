import sys

def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        exit(1)
    except Exception as e:
        exit(2)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python divide.py <a> <b>")
        sys.exit(1)

    a = float(sys.argv[1])
    b = float(sys.argv[2])

    result = divide(a, b)
    print(f"Result of {a} / {b} is {result}")
