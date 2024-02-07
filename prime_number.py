def is_prime_x(num): # this is incomplete approach
    for i in range(2,num):
        if num%i == 0:
            return False
        else:
            return True
print(is_prime_x(1))

def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num**0.5)+1): #This is because any factor of num greater than its square root would have a corresponding factor smaller than its square root.
        if num%i == 0:
            return False 
        else:
            return True       
print(is_prime(1))
