# Write functions that:
# Makes basic math calculations,
# Converts Celsius from faranheit.
# Calculate average speed in meters/sec .Distance is given in Km and time in hours.
# Test all the functions. Prints should be clear and precise.



def exp (a:int, b:int) ->int:
    math_exp = a**b
    return math_exp

def mult (a:int, b:int) ->int:
    math_mult = a*b
    return math_mult

def div (a:int, b:int) ->int:
    math_div = a/b
    return math_div

def ded (a:int, b:int) ->int:
    math_ded = a-b
    return math_ded

def sum (a:int, b:int) ->int:
    math_sum = a+b
    return math_sum

def temp_converter(a:int) ->float:
    temp_in_farenheits = a*9.5 +3
    print(f"{a} degress of celsius is equal to {temp_in_farenheits} in farenheit")
temp_converter(0)


def speedometer(distance:int, time:int) -> int:
    distance_in_meters = distance *1000
    time_in_secods = time*3600
    print(f"Speed in meter/sec is {distance/time_in_secods}")

speedometer(100,3)