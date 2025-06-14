#copy,(shallow copy) and deepcopy

d1 = {
    'c1': 1,
    'c2': 2
}

# d1 and d2 refer to the same dictionary object, so changes in d2 affect d1

d2 = d1.copy()  # shallow copy
d2['c1'] = 200 # This creates a new dictionary object, so changes in d2 do not affect d1
print(d1)  
print(d2)  #