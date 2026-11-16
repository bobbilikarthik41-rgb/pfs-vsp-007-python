'''
Sets
# Sets --> A Set is an Unordered, Unindexed collection, Allow unique values,
# Heterogeneous Collection, Mutable collection

# A Set can contain only tuples in it but not lists, sets...
# We use set() or data inside {} braces

# Every Built-in datatype is a Built-in Function
# subjects = {}  # By default it will be empty dictionary

subjects = set()
print(type(subjects))
print(len(subjects))

data = ['Python', 'Aptitude', 'SQL', 'SS']
subjects = set(data)
print(subjects)
print(len(subjects))
      
ids = {123,125,126,129,['poll','123']} #type Error
#Setdata = ('Python', 'Aptitude', 'SQL', 'SS')
subjects = set(data)
print(subjects)
print(len(subjects))

ids = {123, 125, 126, 129, ['poll', 123]}  # TypeError

# Set Properties --> Membership
print(123 in {124, 123, 125})
ids={123, 121, 125}
new_ids = {126, 127}
#total = ids + new_ids  # TypeError
#print(total)

#Set is a Mutable collection -->Methods-->Insertion,Deletion along With Mathematical set operations
#With Mathematical set operations
#add()-->inserts a single element to the set (unique values)
marks = {45, 25, 35, 20, 21}
print(type(marks))
print(len(marks))
marks.add(250)
print(marks)
print(len(marks))
marks.add((12, 13, 15))
print(marks)
d_marks = [10,5,3,4,6]
marks.update(d_marks)
print(marks)
print(len(marks))
marks.update("codegnan")
print(marks)
print(len(marks))

#marks.update(1,2,3,4) #TypeError
#remove(),discard(),pop()
print(marks.remove(45))
print(marks)
#print(marks.remove(4)) #remove will remove the object if existing else raises KeyError
#discard() removes an element from the set if existing if not it overrides the error

print(marks.discard(45))
print(marks.discard(12345678))
marks.discard(20)
print(marks)
#pop() will removes and returns an arbitrary element from the set
#print(marks.pop())
#print(marks.pop())
#print(marks.pop())
#print(marks.pop())#returns key error as set has become empty
#clear() removes all elements and returns an empty set
marks.clear()
print(marks)

#mathematical set operations -->union(),intersection(),difference()....
a1 = {12,34,23,45}
a2 = {3,45,23,12}
a3 = a1.union(a2)
print(a3)
print(len(a3))
a4 = a1 | a2
print(a4)
a5 = a1.intersection(a2)#returns the common elements in both sets
print(a5)
print(len(a5))
a6 = a2 & a1
print(a6)
a7 = a1.differnce(a2)#removes common elements from both sets and returns elements from first
print(a7)
a8 =a2 - a1 #- is set difference operation
print(a8)
a9 = a1.symmetric_difference(a2)#removes common elements from both sets returns all rmng elements
print(a9)
a10 = a2 ^ a1
print(a10)
#intersection_update() --> performs intersection and updates the first se
a3 = a1.intersection_update(a2)
print(a3)
print(a1)

a3 = a1.symmetric_difference_update(a2)
print(a3)
print(a1)

print(a1,a2)
a1.add(3)
print(a1,a2)
print(a1.issuperset(a2))
print(a2.issubset(a1))
print(a1.isdisjoint(a2))#returns true only when both sets have null intersection

#Dictionaries: A Dictionary is a collection of key-value pairs We use {k:v} as syntax. Keys must be unique,
mutable, ordered,indexed through keys.Keys can be strings, numbers (int, float)
data = {1: 'Vinay',
        2: 'Vijay',
        3: 'Ajay'}

print(data)
print(type(data))
print(len(data))
print(data[2])
print(type(data[1]))

details = { 'ids': ['CGV10242', 'CGV10249',
                    'CGV10224', 'CGV10240'],
            'names': ['Nikitha', 'Deepthi',
                      'Vinay', 'Tej'],
            'batch': 'PFS-VSP-007',
            'place': ('Vizag', 'Vjwda', 'Hyd', 'Bnglre'),
            'subjects': {'Python', 'Aptitude', 'Softskills'}}

#print(details)
#print(len(details))
print(details.keys())
print(details['ids'])
print(type(details['ids']))
details['ids'].append("CGVI0245")
print(details['ids'])
details['ids'].insert(3, "CGVI0247")
print(details['ids'])
print(details['ids'][:3])#returns first 3 ids
print(details['ids'][::2])
'''







