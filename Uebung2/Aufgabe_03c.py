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

print(list1, list2, sep='\n')
list1.remove([1,2,3])
print(list1)

rlist = list1
clist = rlist.copy()
clist.insert(0,-3)
clist.insert(0,-2)
clist.insert(0,-3)
print(clist)