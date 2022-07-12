Python 

Datatypes and Variables

Lists and slicing lists

Functions
Commonly used built-in-functions: max(), min(), round(integer, n_decimals)

Methods
- function that is attached to an object depending on the type. Also, all variable in Python are considered as objects
ex $ object.index("any string or integer etc") --This gives the index of the value placed inside
ex $ object.append("any string or int etc") --This inserts a value at the end of a list

Packages
steps:
1. download package
2. install package
3. import package | from package import specific_function | from package import spec_func as spec_rename

Tips:
help() built in function
ex $ help(round)
ex $ ?round

FreeCodeCamp

IF STATEMENTS
if True:
    print("this will mostly appear)
elif alternative True:
    print("then this will print)
else:
    print("when both is not true, this will print")

LOOPING / ITERATOR
- while
- while loop condition
- for range

LIST - acts like an array also with index starting from 0

DICTIONARY: Key-value data structure
- values in the dictionaries can be accessed using the keys. 
- I can interpolate using the format structure or f-strings format

ITERATION: Looping through data structure
$ for any_name in list/array:
    print(any_name)
$ for any_key in dictionary:
    print("{} and {}".format(any_key, dictionary[any_key]))
    