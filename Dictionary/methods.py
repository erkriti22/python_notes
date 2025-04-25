dict = {"name":"student", "age": 25, "class": "4th"}

print(dict["name"])

# .get(): This method helps get the value with the key provided as the para or we can use loops
print(dict.get("name"))

#  to fetch values fromm the keys, pass it like dict[key]
for i in dict:
    print(i, dict[i])

# .items(): to fetch both key and value from the dict. the pair of key and value is known as items
for key, value in dict.items():
    print(key,":",value)

# if you give a key that is not there in the dict the output is none
print(dict.get("surname"))

# if you want to replace the value, use the key to do so
dict["class"]= "5th"
print(dict)

# if you want to insert any item, then add along with key
dict["city"]= "Bhopal"
print(dict)

# Nested Dict
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child1"]["name"])