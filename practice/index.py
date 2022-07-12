
msg = "Hello World"
print(msg)


# if 1 > 2:
#   print("1 is greater than 2")
# elif 2 > 1:
#   print("1 is not greater than 2")
# else:
#   print("1 is equal to 2")

# num = 1

# while num <= 10:
#     print(num)
#     num += 1

# for i in range(1, 11):
#   print("i",i)

# loop_condition = True

# while loop_condition:
#     print("Loop Condition keeps: %s" %(loop_condition))
#     loop_condition = False

shepherd = "Mary"
age = 30
string_in_string = "Shepherd {}, {} is on duty.".format(shepherd, 30)
f_strings_format = f"This is how it looks like in f {shepherd} and {age}"
print("format", string_in_string)
print("f-strings", f_strings_format)

dictionary_tk = {
  "name": "Leandro",
  "nickname": "Tk",
  "nationality": "Brazilian"
}

#appending Dictionaries
dictionary_tk["age"] = 24

#print(f"His name is {dictionary_tk['name']}, and you can call him {dictionary_tk['nickname']} too")
#print(dictionary_tk)

for any_key in dictionary_tk:
    print("My {} is {}".format(any_key, dictionary_tk[any_key]))

#IteriItems
for attribute, value in dictionary_tk.items():
    print("My %s is %s" %(attribute, value))
