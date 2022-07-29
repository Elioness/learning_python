# Python Built-in Functions

# Range(start, stop, step)

# Enumerate(<list>, start=0)
# - start is optional 
# - unpack an 

# map(<another built-in function, lambda>, <list>)
# - map needs to be placed inside a new variable
# - map also needs to be itirated inside a list function

nums = [1.45,2.8,3.9,4.94,5.6]
rnd_nums = map(round, nums)
print("maps", nums, list(rnd_nums))
print(type(rnd_nums))




