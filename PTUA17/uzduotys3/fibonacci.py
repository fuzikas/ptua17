a=0
b=1
print("Fibonacci seka", end=" ")
print(a, b, end=" ")

for _ in range(8):  
    a, b = b, a + b  
    print(b, end=" ")