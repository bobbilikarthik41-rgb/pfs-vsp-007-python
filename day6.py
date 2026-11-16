'''
Tokens,Datatypes(Numeric,Boolean,NOnetype,Sequences(str,lists,tuples,sets,frozensets,mapping objects (dicts))Typecasting
operators
input formatting / output Formatting

#Input Formatting --> input()
#usage of input()
#we can pass any type of object as input-->result is in only string

name = input("Enter the name:")
prinintt(name)
print(type(name))

#Integer Input --> int()--> if u mismatch value --> ValueError
roll_number = int(input("enter the roll number:"))
print(roll_number)
print(type(roll_number))
#Float input --> float()--> we can pass either integer / decimal value
marks =float(input("Enter the marks:"))
print(marks)
print(type(marks))

#Group of strings(Multiple values as strings)
#space seperated values --> we need to give one space after each object returns list
names = input("enter the names:").split()
print(names)
print(type(names))

#Comma seperated Values
subjects = input("enter the subjects:").split(',')
print(subjects)
print(type(subjects))

#multiple values (more than one)strings
name,batch = input("Enter the details:").split()
print(name)
print(batch)

#multiplle interger values
order_id,cost = map(int(input()).split())
print(order_id)
print(cost)

#we want to take subjects marks
py_marks,ap_marks,ss_marks,sql_marks = map(float,input().split())
print(py_marks,ap_marks,ss_marks,sql_marks)

#Group of integer,float values
stu_marks = list(map(int,input("Enter the marks:").split(',')))
print(stu_marks)

discounts = list(map(float,input("Enter the discounts:").split(',')))
print(discounts)

#Accept the cost of selling the product from user and also the original cost of the product and determine the profit/loss amount for the user
original_amount = float(input("Enter the original cost:"))
selling_amount = float(input("entrer the selling cost:"))
profit = selling_amount - original_amount
print(profit)

#set of integers
#set of float values -->replace int with float
ids = set(map(int,input("enter the IDS:").split(',')))
print(ids)
print(type(ids))

#Passing list() as input using eval()
list_data =  eval(input("enter the list values"))
print(list_data)
print(len(list_data))
tuple_data =  eval(input("enter the tuple values"))
print(tuple_data)
print(len(tuple_data))
set_data =  eval(input("enter the set values"))
print(set_data)
print(len(set_data))

#passing dict data using eval
stu_details = eval(input("Enter the values:"))
print(stu_details)

#So using eval() u can pass any type of data
#Output Formatting --> print()
a,b,c = map(str,input("Enter the names:"))
print(a,b,c)
#now we will use sep --> sep is the keyword
print(a,b,c,sep="----")
#end is specifically telling how u wanna end the statements
print(a,b,c,sep=":",end='\t')
print("Saketh","Vizag",end=" ")
print(34,4.5)

#1) Using commas in print() --> we seperate by commas
name = "codegnan";branch = "vizag";batch = 'PFS-VSP-007'
print(name,"is in",branch)
print(batch,"belongs to",branch,"branch")
'''
# 2) Using % (modulus) formatting --> Old Style C Programming
# %d --> integers, %f --> float, %s --> strings
age = 32
price = 45.256
place = "Vizag"
print("Age = %d | Price = %f | Place = %s" % (age, price, place))
print("Price is %.f"%price)#In this case, the complete decimal part is wiped out.
print("Price is %.2f"%price)#rounding off to two decimals
