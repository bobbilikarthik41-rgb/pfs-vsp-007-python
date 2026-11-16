'''
#usage of Variable length and Keyword Variable length arguments

def scores(*marks,**names):
    """Scores Scenario with Variable and keyword variable length args"""
    print(marks)
    print(names)
    total = 0
    for mark in marks:
        if type(mark) in (int,float):
            total += mark
    print(f'Total Marks are: {total}')
    #for name,value in names.items():
    for name in names.values():
        print(f'Name : {name}')
        #print(f'Value :{value}')

scores(25,20,15,18,16,name="Ajay",place = "Vizag",batch="PFS-VSP-007")
#positional aruguments always follows keyword argumnts
#Non default always follows default args

#Scope --> Determines where a variable can be accessed within a program
#A variable is only accessible within the region where it is defined...

Types of Scope : Local Scope, Global Scope, Global Keyword, Nonlocal Scope


#Local Scope: Variables defined and accessible only inside the function..

def fname():
    """Usage of local variables"""
    name = "Codegnan"
    return f'{name} is in Vizag'
print(fname())
#print(name)
print(fname())
name = "saketh"
print(name)

#Local variables get higher priority
name = "codegnan"
def uname():
    """Global Scope"""
    return f"{name} is in Vizag, Vijayawada and Hyderabad."

print(uname())
print(name)

# Global keyword --> Used when we want to modify a global variable
count = 15
def update():
    """Global Keyword usage"""
    global count
    count = 5
    return f'Updated count is {count}'
print(update())
print(f'New count is {count}')
values = [1,3,45]
values.append(count)
print(values)

# NonLocal --> Used in Nested Functions...Allows modifications of
# variables from the outer function
count = 25
def outer():
    """Outer Function"""
    count = 25 + 4
    def inner():
        """Inner Function"""
        nonlocal count
        count = count + 15
        return f'Result from Inner function is {count}'
    print(inner())
    return f'Result from Outer function is {count}'
print(outer())

#LEGB --> Local,enclosing-->Global --> built in
len = 45
a = ['codegnan','python']
#print(len(a)) #Here we have used built-in function as identifier it fails

#Functions are termed as first class objects
#pass by value and pass by object reference

#pass by value --> immutable objects
#when immutable objects are passed to function,changes inside the function
#do not effect the original value
def update(number):
    """Pass by value usage"""
    number = 15
    print("Inside Function:",number)
x =20
update(x)

# Pass by value usage
def update(number):
    """Pass by value usage"""
    return number * 3
    #print("Inside Function:", number)

number = 20
print(update(number))
print(update(25))
'''


