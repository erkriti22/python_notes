L1 = ["Ashok", "Binod", "Chandu", "Deep"]

# .append(), to add any new elemet in the list, the new element will be added in the end.
# L1.append("Suresh", 45) this gives error as append takes only one argument
L1.append("Suresh") 
print(L1)

# .pop(), to remove the last value from the list, it will echo the element being removed
L1.pop()
print(L1)

# To remove specific values we mention the element in the list to be removed.
L1.remove("Binod")
print(L1)

#  To insert elements in the list, takes 2 parameters index and the element.
L1.insert(2,"rabbit")
print (L1)