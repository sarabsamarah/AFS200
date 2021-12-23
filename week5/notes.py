# def sum_function(first, second):
# return(return+second)

# print("Sum:", sum_function(5,10))
# w = {'temp': "30 degrees Celsius ", 'in': 'in 'State':" New York"}
# def print_weather_kwargs(**kwargs):
#     weather = " "
#     for argument in kwargs.values():
#         weather += argument
#     return weather

#     x = lambda a, b, c: a + b + c
# print(x(5, 10, 20))

def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
print(mydoubler(11))
