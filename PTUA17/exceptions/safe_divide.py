# try:
#     print("I am here!")
#     print(2 / 0)
# except Exception as e:
#     print(f"Learn some basic math dude!,because off error: {e}")


# try:
#     # print("I am here!")
#     print(2 / 0)
# except ZeroDivisionError:
#     print(f"CAN'T DIVIDE BY ZERO!")


# try:
#     input = int(input("Enter a number: "))
#     print(input)
# except Exception as e:
#     print(f"Error: {e}")



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