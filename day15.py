n = int(input("Enter a value:"))
'''for i in range(1,n+1):
    for j in range(1,n+1):
        #print(i,j,end=" ")
        if j <= n-i:
            #print(i,j)
            print(" ",end="")
        else:
            print("*",end=" ")
    print()

for i in range(n):
    print(" "*(n-i-1)+"*"*(i+1))
#Now same approach u can try for diamond pattern:
'''
n= int(input())
#upper part
for i in range(n):
    print(" "*(n-i-1)+"* "*(i+1))
#lower part
for i in range(n):
    print(" "*(i+1)+"* "*(n-i-1))
