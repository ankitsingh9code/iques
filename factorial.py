def factorial(number):
    result = 1
    for i in range(1,number+1):
        result *= i     
    return result

def factorial_recursion(number):
    if number ==  0 or number == 1:
        return 1
    else:
        result = number*factorial_recursion(number-1)
        return result

print(factorial(4), factorial_recursion(4))

# def factorial1(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial1(n-1)
    
# print(factorial1(3))