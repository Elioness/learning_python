# Lambda functions - are single used one-line functions

#name_of_function = lambda parameter: expression

add_function = lambda x, y: x + y #lambda implicitly returns ALL the time
print(add_function(10, 5))

# Lambda function as a return inside a function
def price_calc(start,hourly_rate):
    return lambda hours: start + hourly_rate * hours
    
walk_in_cost = price_calc(10,30)
print(walk_in_cost(2))

# Other ways to write Lambda
print((lambda a,b,c: a+b+c)(2,3,4)) #I can also add a default value, remember to put it last
print((lambda *args: sum(args))(2,3,4,50)) # Unpack the parameter to use a method in it