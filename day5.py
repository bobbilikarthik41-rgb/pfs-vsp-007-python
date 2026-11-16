'''
Operators--> Operators help us to perform operations between operands

Arithmetic Operators -->+,-,*,/,**,//(Integer or floor Division),%(modulus --> remainder)

Assignment operators -->It helps to assign,update(increment),decrement values

# = (assigning),+= (Addition&assign),-=(subtraction&Assign),
# *=(Multiplication&Assign) /=,//=,**=,%=

data = 20
print(data)
print(type(data))

stock = data
print(stock)

#Increment the value of stock
stock = stock + 5#stock+=5
print(stock)
print(data)

#decrement the value of data by 2 values
data=data-2
print(data)

data*=2
print(data)

data/=2
print(data)

data//=2
print(data)

data**=2
print(data)

data%=2
print(data)

stock=100
stock**=2
print(stock)

#Comparision operators (relational operators)--> It performs comparision
#between the operands and results in boolean true/false -->Conditions
# ==, != ,<,<=,>,>=
name = 'karthik'
karthik_attendance = 75
print(karthik_attendance == 80)
print(karthik_attendance >= 80)
print(karthik_attendance <= 80)
print(karthik_attendance <80)
print(karthik_attendance > 80)
print(karthik_attendance != 80)

#Logical Operators-->and,or,not(keywords)
#and--> it needs all conditions to be satisfied (two or more)
#or --> it needs any one condition to be satisfied
#not --> opp to existing

max_marks =80
karthik_marks = 75
max_att =75
karthik_att = 70

certificate = karthik_marks >= max_marks and karthik_att >= max_att
print(certificate)
chance = karthik_marks >= max_marks or karthik_att >= max_att
print(chance)
data=[]
print(data)
print(not(data)) #returns True
data = [1,2,3,4]
print(not(data))#returns False as data is existing
#Both logical and comparision operators will return result in boolean

#Membership Operators--> in,not in
#check for the existence in a squence (str,list,set,tuple,dict)

names = ['vinay','vijay','karthik','raju']

name ='ajay'
print(name in names) #returns false
print(name not in names) #returns True
print('12' in '121')
#print(12 in 121) #Typeerror as we have taken int type

#identify operators --> It specifically refers to the object(memory location)
#id --> is,is not

a= 15
b= 15
print(a==b)
print(id(a))
print(id(b))
c = a
print(id(c))

print(c is a) #as id of both a and c are same -> true

a = [1,2,3,4]
b = [1,2,3,4]
print(a == b)
print(id(a))
print(id(b))
#as we have taken two lists eventhough with similar values identity
print(a is b)

c = a
print(id(c))
print(c is a) #returns True as we are assigning same object

a=(1,2,3)
b=(1,2,3)
print(id(a),id(b))
print(a is b)
#when we check the interpreter mode and scripting mode above tuple result changes

# logical, Membership,Idnentify,Comparision(relational) --> always result is in boolean
#An integer will be converted binary format and performs bitwise operation following integer to bianry conversion
print(7&3)
print(7|3)
print(7^3)
#7 to binary -->0111
3


