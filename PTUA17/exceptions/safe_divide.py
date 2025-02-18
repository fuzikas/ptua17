import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="data.log",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def safe_divide(first_number:int, second_number:int)->float:

    try:
        result = first_number/second_number
        print("Attempted division")
        return result
    except ZeroDivisionError:
        logging.critical(f"No go, zero division error {ZeroDivisionError} ")
        print("Division by 0 is not possible")
    except TypeError:
        logging.critical(f"No go, one or both of the arguments != number {TypeError} ")
        print("both arguments must be numbers")
