L1 = [1, "acg", 2, "ABC"]

# slicing and negative slicing is allowed
# list(start:end:step)

# Indexing starts with 0

print(L1[2])
print(L1[:3])

L1[0]= 56
#  replace any element using indexing
print(L1)

# L1[1:2] = "rttk"
# print(L1)
# output is this [56,'r', 't', 't', 'k', 2, 'ABC'] which is wrong hence
# we will give input as a list
L1[1:2] = ["rttk"]
print(L1, "a")
L1[1:2]= ["agah","hdhd",565]
print(L1, "b")
# wecan do the same with multiplevalues as well.
# o/p: [56, 'agah', 'hdhd', 565, 2, 'ABC']

print(L1[1:1], "op will be empty array")

L1[1:2]= ["test", "test1"]
print(L1, "values will be inserted and existing values will shift")


L1[1:3] = []
print(L1, "it is like deleting the elements from these indexes, also known as insert nothing")

for i in L1:
    print(i, end = " " )

print("this end will give option to add any separator within the elements of the output, ex: space, "" or -")