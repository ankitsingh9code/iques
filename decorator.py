# decorator function to capitalize names
def names_decorator(function):
   def wrapperqq(arg1, arg2):
       arg1 = arg1.capitalize()
       arg2 = arg2.capitalize()
       string_hello = function(arg1, arg2)
       return string_hello
   return wrapperqq

@names_decorator
def say_hello(name1, name2):
   return 'Hello ' + name1 + '! Hello ' + name2 + '!'
x= say_hello('sara', 'ansh')   # output => 'Hello Sara! Hello Ansh!'
# print(x)


def strmanupulator(function):
    def wrapper(str1):
        str1 = str1.upper()
        function(str1)
        print('inside wrapper')
        # return str1
    return wrapper        

@strmanupulator
def originalf(str1):
    print(str1)
    
originalf('fff')
    