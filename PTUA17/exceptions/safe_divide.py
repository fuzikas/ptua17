

def safe_divide(first_number:int, second_number:int)->float:
    try:
        result = first_number/second_number
    except ZeroDivisionError:
        print("Division by 0 is not possible")
    except TypeError:
        print("both arguments must be numbers")
    else:
        print("Division successful")
        return result
    finally:
        print("Attempted division")

print(safe_divide(10,3))