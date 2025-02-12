# 1) Create a lambda function that takes a number and returns its square.
# 2) Create a lambda function that takes two numbers and returns their squared sum.
# 3) Use the lambda function to sort list of tuples based on the second element:
# tuples_list = [(1,3), (4,1), (5,2), (2,4)]

# 1
square = lambda num_1: num_1 * num_1
print(square(3))

# 2

squared_sum = lambda num_uno, num_dos: (num_uno*num_uno) + (num_dos*num_dos)
print(squared_sum(3,4))