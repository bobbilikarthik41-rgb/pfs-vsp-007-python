'''
String methods --> case conversions,replacing,finding,white trailing spaces,testing spaces,testing methods,alignment methods

#case Conversions -->upper(),lower(),title(),capitalize(),swapcase()
data = "codegnan"
print(type(data))
print(dir(data))

#uppper()--> converts objects to upppercase
print(data.upper())
e = data.upper()
print(e)
#lower()-->converts object to lowercase
f = data.lower()
print(f)

#capitalize()-->it wil capitalize the first letter in the word
print("codegnan vizag".capitalise())
#title() --> it  wil capitalize every first letter in each word
print("codegnan vizag".title())

#Testing methods (which wil give the resullt as boolean(true/false)
#isupper(),islower(),isalnum(),isdigit()....
print("Codegnan".isupper())
print("codegnan".islower())
print("admin123".isalpha())#returns true only when we have all alphabets
print("admin123".isalnum())#returns true for an alphanumeric string
print("81234".isdigit())
print("Python".istitle())#returns true
print("Python aptitude".istitle())#returns False
print("Python".startswith('P'))

data = "Python Aptitude"
print(data.startswith("A"))
print(data[7:].startswith("A"))
print(data.startswith("A",7))
print(data.endswith("e"))
print(data.endswith("n",0,6))

print("12.34".isalnum())
print("12.34".isdigit())
print(" ".isnumeric())#fractions,roman numericals
print("XII".isnumeric())#roman numerics but we need to encode the data and get it

#finding and searching methods --> find(),index(),count()
data = "Codegnan is in vizag"
print(data.find('a'))#returns only the first occurance
print(data.find('a',7))#here we will check for the next occurances
#find() will return -1 if the give object is not present
print(data.rfind("a"))#rfind() will return the last occurance
#index(),rindex()
print(data.index("a"))#returns the first occurance
#if given object is not present it raises valueError
#print("qwerty".index("s"))#raises ValueError
print("qwerty".index("werty"))#as substring is starting with 'w'
#rindex() returns last occurance
print("qwertywerty".rindex("y"))
#count() will return total number of occurances
print("codegnan".count("n"))
print("codegnan".count("t"))#returns 0 as 't' is not present

#split(),join(),strip(),lstrip(),rstrip(),zfill()
a = "python aptitude softskills MYSQL"
b = a.split()
print(b)
a = "python,aptitude,softskills.MYSQL"
c = a.split(',')
print(c)
#join
print("code".join("gnan"))#concatenates every object with the given iterab
print("#".join("Codegnan"))
print(" ".join("karthik"))

#white space & Trimming methods -->strip(),lstrip(),rstrip()
a = "karthik"
print(len(a))
a = a.strip()#removes leading and trailing whitespaces
print(len(a))

#Alignment Methods -->zfill() (Make sure to pass the width > len(obj))
print("python".zfill(10))
print("codegnan".zfill(1))
print("python".center(10,'*'))

print("python".ljust(10,"*"))
print("python".rjust(10,"*"))
'''
#sequences --> Lists[],tuples(),sets set(),Frozensets,Dicts {}






