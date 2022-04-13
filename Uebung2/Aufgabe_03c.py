# create list
list1 = [0]
list2 = [0]
# put new numbers to list
'''
append appends an object 
extend extends a list by appending elements 
'''
list1.append([1,2,3])
list2.extend([1,2,3])

list1.remove([1,2,3])

rlist = list1
clist = rlist.copy()
clist.insert(0,-3)
clist.insert(0,-2)
clist.insert(0,-3)

# remove 0 from clist
clist.pop(clist.index(0))

print(list1, list2, rlist, clist, sep= '\n')

# by clearing original list the copy will be cleared too
list1.clear()
print(list1, list2, rlist, clist, sep= '\n')