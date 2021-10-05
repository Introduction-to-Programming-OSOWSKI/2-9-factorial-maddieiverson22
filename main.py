#WRITE YOUR CODE IN THIS FILE
def factorial(x):
    y = 1
    for i in range(x, 1, -1):
       y = y * i 
    return y
print(factorial(5))