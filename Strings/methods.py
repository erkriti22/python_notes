# we can apply n number of methods in a string, but it will not change the original string as strings are immutable.

unm = "Kriti Sharma"

print(unm.lower())
print(unm.upper())

dec = "    kriti sharma   "

print(dec.strip())
# strip() method removes the extra spaces from the string. it is useful when we take user input

print(unm.replace("Sharma","kelkar"))
# replace() method takes two parmeters, first the one we wish to replace and second that we wish to add after replacing.
# if the 1st parameter is not there in the string, then it wont be replaced

student_info= "Ashok, Bharat, Chandu, Deep"
print(student_info.split())
print(student_info.split(", "))

# .split() converts string into a list, takes 2 parameters (separator, maxsplit).
# The separtar can be "," , ", ", "="

print(unm.find("a"))
print(unm.find("Kriti"))
print(unm.find("ssss"))
# .find() finds either the word or a specific character.
#  if the asked is not present the output will be -1.

st = "My name is Ria, I'm in class 10th, I'm good in Maths."
print(st.count("a"))
print(st.count("My"))
print(st.count("May"))
# if not present count, results  0

emp = ["Ashok", "Bharat", "Chandu", "Deep"]
print("-".join(emp))
# "".join() it is used to convert list to string. 
# "" we can give any separator in between double quotes.


