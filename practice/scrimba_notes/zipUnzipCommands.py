# Zip and Unzip

nums = [1,2,3,4,5]
letters = ["a","b","c","d"]
names = ["Lily", "Erick", "Matt", "Sonya"]
combo = list(zip(nums, letters, names))
print(combo)

# Unzip or unpacking

numzUn, lettersUnzip, names = zip(*combo)

print(numzUn)

# Zip / Unzip Dictionaries

keys = "This parrot is funny"
values = "Denna papegojan ar rolig"

keys = keys.split()
values = values.split()

en_sv_dictionary = dict(zip(keys, values))
print(en_sv_dictionary)

# Zip using comprehension method
new_dict = {key:value for key,value in zip(keys, values)}
print("new_dict", new_dict)

#Unzip 
#1
en, sv = (list(en_sv_dictionary.keys()), list(en_sv_dictionary.values())) 
print(en, sv)
#2
en1, sv1 = zip(*en_sv_dictionary.items())
print("*", en1, sv1)


