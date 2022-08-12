# Comprehensions - the same code for loop. Evolution of maps and filters altogether and is easier to read
# Structure:
# var_name = [what the output is going to be, in this case a list] for param,param,param in zip(whatever variables I want to combine)
# add if statement in the end if there is a condition

from ast import comprehension

numbers = [1,2,3,4,5,6,7,8,9]
# give me a list with num squared for each num in numbers
new_list = []
for num in numbers:
    new_list.append(num*num)
print(new_list)
# give me a list with num for each num in numbers if num is even 
new_list = [num for num in numbers if num % 2 == 0]
print(new_list)

new_list = filter(lambda num: num % 2 ==0,numbers)
print(list(new_list))

# I want a (letter, num) pair for each letter in 'spam' and each number in '0123'
new_list = []
for letter in 'spam':
   for num in range(4):
       new_list.append((letter,num))
print(new_list)

new_list = [(letter,num) for letter in'spam' for num in range(4)]
print(new_list)

# Dictionary Comprehensions

movies = ["And Now for Something Completely Different","Monty Python and the Holy Grail",
"Monty Python's Life of Brian","Monty Python Live at the Hollywood Bowl","Monty Python's The Meaning of Life","Monty Python Live (Mostly)"]
year =[1971,1975,1979,1982,1983,2014]
names = ['John','Eric','Michael','Graham','Terry','TerryG']

# Create dictionary using a for Loop
new_dict = dict()
for movie, yr in zip(movies, year):
    new_dict[movie] = yr
print(new_dict)

# Create dictionary using Comprehension
comprehension_dict = {movie:yr for movie,yr in zip(movies, year)}
print(comprehension_dict)

# Only get moview that are created before 1883
comprehension_dict = {movie: yr for movie, yr  in zip(movies, year) if yr < 1983 and movie.startswith("Monty")}
print(comprehension_dict) 