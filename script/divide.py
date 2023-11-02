def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Failed: Division by zero"
    except Exception as e:
        return f"Failed: {str(e)}"

# Successful division
a = 10
b = 2
result = divide(a, b)
print(f"Result of {a} / {b} is {result}")

# Attempting division by zero
a = 5
b = 0
result = divide(a, b)
print(f"Result of {a} / {b} is {result}")

