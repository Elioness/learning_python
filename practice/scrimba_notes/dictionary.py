
#Dictionary - key-value pairs
#ex

movies = {
    "title": "Life of Pi",
    "year": "2002",
    "cast": ["john meyer", "sandra bullok", "quinn william", "willow smith"]
}

#Acces it like an index or through Get method
print(movies["cast"][1])
#Get method, doesn't give an error when the key is not in the dictionary. 
#Also, you can add a default value instead of returning "none"
print(movies.get("key", "I can not find this key"))

#Updating and Deleting
movies["year"] = "1994"
movies.update({"title": "Duck with Green Lips"})
movies.update({"rating": 8})
#del movies["rating"]
rating = movies.pop("rating")
print(movies)
print("rating", rating)

#Common dictionary methods
movies.keys()
movies.values()
movies.items()

#Loops
for key, value in movies.items():
    print(key)
    print(value)

python = {'John':35,'Eric':36,'Michael':35,'Terry':38,'Graham':37,'TerryG':34}
holy_grail = {'Arthur':40,'Galahad':35,'Lancelot':39,'Knight of NI':40, 'Zoot':17}
life_of_brian = {'Brian':33,'Reg':35,'Stan/Loretta':32,'Biccus Diccus':45}

people_update = {}
people_comprehension = {}
people_unpacking = {}

# 1st method = Update
people_update.update(python)
people_update.update(holy_grail)
people_update.update(life_of_brian)
print("update", people_update)

# 2nd method - Comprehension
for groups in (python, holy_grail, life_of_brian) : people_comprehension.update(groups)
print("comprehension", people_comprehension)

# 3rd method - unpacking
people_unpacking = {**python,**holy_grail, **life_of_brian}
print("unpack", people_unpacking)
sorted(people_unpacking.items())
print(sum(people_unpacking.values()))
