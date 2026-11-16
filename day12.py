'''n = int(input("Enter the sales"))
if n > 1000:
    print("Best Seller")
else:
    print("No output")
'''
'''
rain = input("Extra Rain Charges Applied")

if rain == "True":
    print("Extra Rain Charges Applied")
'''
'''
order_value = int(input("Enter order value: "))
if order_value > 99:
    print(f'Final bill amount:{order_value}')
else:
    print(f'final bill amount:{order_value + 30}')
'''
'''
budget = int(input("Enter your budget: "))

if budget > 10000:
    print("Plan: Trip")
elif budget > 5000:
    print("Plan: Resort Stay")
elif budget > 3000:
    print("Plan: Movie and Dinner")
elif budget > 1000:
    print("Plan: Cafe and Shopping")
elif budget > 500:
    print("Plan: Street Food and Park Visit")
else:
    print("Plan: Stay Home")

# range(stop) --> takes by default minimum value as 0
for i in range(5):
    print(f"Value of i is {i}")
    print(f"Square of i is {i**2}")

#range(start,stop) -->u can mention start and stop postns(values)
#start is included,end is excluded
for i in range(1,11):
    print(i,i**2)
    print('<----->')

#range(start,stop,step)
for i in range(1,21,1):
    print(i)
for i in range(1,21,2):
    print(i)
    
#print numbers from 10 to 1 in reverse order
for i in range(10,0,-1):
    print(i,end=' ')
#print 'A' to 'Z' in a single line
for i in range(65,91):
    print(chr(i),end=' ')

names = ['Akash','Karthik','Vijay','Sanjay','lokesh']
for  name in names:
    print(name,end=' ')#this returns in horizontal order
for i in range(len(names)):
    print(names[i]) #names[0] -->Akash-->names[1]-->karthik

#Ask integer input from user and get the sum of numbers as per input
n = int(input("Enter a value:"))
if n>=0:
    result = 0 #target
    for i in range(n+1):
    #print(i)
    result = result + i
    print(f'result of {i} is {result}')
else:
    print("No Output")
'''
# Usecase: Checking daily workout app usage
work_log = [1, 1, 1, 0, 1, 1, 0]
# 1 --> workout done
# 0 --> workout missing
# Find the longest workout streak
longest_streak = 0  #target
current_streak = 0
for day in work_log:
    # print(day)
    if day == 1:
        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak = current_streak
    else:
        current_streak = 0
print(f'Longest Streak is {longest_streak}')


















    
