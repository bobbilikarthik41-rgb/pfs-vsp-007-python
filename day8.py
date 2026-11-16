'''
Sequences -> Strings,list[],Tuples(),sets set(),Dictionaries{}
Lists[] --> A list is an ordered,mutable,indexed and hetrogenous collection
It will be dynamic in size

#Creation of lists
details = [123,"karthik",32,"PFS",75.5]
print(type(details))
print(len(details))
print(details)

#Nested Lists
batches = [["PFS","PFS-VSP-007","PFS-VSP-008"],
           ["DA","DA-VSP-007","DA-VSP-008"],
           "Vizag",8]
print(len(batches))
print(type(batches))

#Indexing,Slicing,striding
print(batches[0])
print(batches[-3])

print(batches[1:4]) #observe the output
print(batches[:2])
print(batches[1:5:2])

print(batches[-5:-1:4])
print(batches[-1:-5])
print(batches[1:4])
print(batches[0][1])

#subindexing -->Accessing index within the index of a collection

print(batches[0])
print(batches[0][1])
print(type(batches[0][1]))
print(batches[0][1][4:7])
print(batches[0][1][5:7])
print(batches[1][2])
print(batches[1][2])

print(len(batches[0][1]))
print(batches[0][1][:3]+batches[0][1][-4:])

print([1,2,3] *3) #repetition
#print([1,2,3]+3 #TypeError
print([1,2,3] + batches)#Merging
a = [1,2,3]
b = a*3
print(len(b))

print(batches)
print('Vizag' in  batches) #Membership
print('PFS' in  batches)
print('PFS' in  batches[0])#returns true

#lists methods
data = []
print(dir(data))#returns list of all available methods
#append(),extend(),insert()
#append(obj)--> insert object to the end of the list
data.append(24)
print(data)
data.append('Vizag')
print(data)
#data.append('python','MYSQL')#TypeError
data.append(["python","Mysql"])
print(data)
print(len(data))
print(data.extend(['python','MYSQL']))
print(data)

data.extend('vizag')
print(data)
#insert(index,object)-->inserts elements before index
data.insert(2,'saketh')
print(data)

data.insert(-3,'saketh')
print(data)

data.insert(2,[34,45,6])
print(data)

# Lists are mutable
marks = [25,24,27,28,30,35,36]
print(marks)
marks[2] = 45
print(marks)
marks[:3] = ['saketh','codegnan']
print(marks)

#In above cases data is being modified in original list
#(Indexing case length remains constant but data is modified,
#whereas in slicing case it may increase or decrease)

#pop(),remove(),clear()-> removes elements from the list
subjects = ['Python','Aptitude','SS','Mysql','Flask']
#pop()--> removes by default last element if index is not mentioned
#print(subjects.pop())# removes and returns last element
#print(subjects.pop(2))
#print(subjects.pop(5))# raises IndexError
#print(subjects)
#remove()-->removes specific value from the collection (only first occurrence)
subjects.remove("Python")
#print(subjects.remove("python")) # returns None
#subjects.remove("Codegnan")  # ValueError
#clear()-->removes all elements from the list and returns empty list
subjects.clear()
print(subjects)


#copy(),sort(),reverse()
details = [['sanjay','python',50],
           ['Akash','Flask',45],
           ['vinay','aptitude',30]]
print(details)
print(len(details))

#copy() -->creates a shallow copy of the given collection
data = details.copy()
#print(data)
#print(len(data))

data[0].append("A")#nested list changes will be directly applicable in both lists
data.append("vizag")
print(data)
print(len(data))
print(details)
print(len(details))

data.extend(["PFS',"JFS"])
print(data)
print(len(data))
#print(details)
#print(len(details)
'''
#sort() reverse()
#marks =[12,15,20,24,21]
#print(marks.sort()) #returns None as nothing to be returned
#print(marks)
#marks.sort(reverse=True) #it returns in descending order
#print(marks)

#marks.append("karthik")
#marks.sort() #raises typeError
'''
marks.extend([-23,12,87])
print(marks)

marks.sort(reverse=True) #descending order
print(marks)

print(marks)
marks.reverse()
print(marks)
marks.extend(['pool','Sunday',123])
marks.reverse()#this will make changes in original list
print(marks)
print(marks[::-1])#this will just return the reverse order as o/p

#min(),max(),len(),type(),sorted()
marks = [20,12,23,25,30]
print(min(marks))
print(marks)#sorted() function returns a new list with elements in ascending order
print(b)
print(marks)

#tuples --> tuples are immutable,ordered,indexed collection,it can also have duplicates,we use() to store the data
data = ()
print(type(data))
print(len(data))

data = 1,2,3,4 #by default it stores in tuple
print(data)
print(type(data)

#be very specific when we are passing data using()
#tuples are immutable we cannot modify the elements in it
#data[-2] = 'codegnan' #it is not possible
#nested tuples (also will have lists in it)

details = ("vizag",8,("PFS","JFS","DA"),["Aptitude","Softskills"])
print(len(details))
print(details[:2])
print(details[2][1])

print(details[-1])
details[-1].extend(['python','java'])
print(details)

#we cannot make any changes over tuple directly but we can change on list
print(details[0].upper())
print(details)

#indexing,slicing,repetition,merging are possible
temp = (23.5,24,34.5)
b= temp*2
print(b)
print(b + temp)
'''

#tuple methods --> index(),count()
data = (12,3,24,3,12,4,5)
print(data)
print(data.index(3))
print(data.index(3,2))
print(data.count(3))

b = sorted(data)
print(tuple(b))
c = tuple(sorted(data,reverse=True)) #returns tuple in descending order
print(c)

#sets : A set is a unordered,unique,mutable collection.it will never dulplicates
ids = set()
print(ids)
print(type(ids))

names={'saketh','raju',24,3,'raju',24}
print(names)
print(len(names))
