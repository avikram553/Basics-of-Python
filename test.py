a = 10
b = 20
print(a+b)
print("Subtraction is - ",a-b)
print("Multiply - ",a*b)
print("Division - ",a/b)

#Swapping
print("Values of a and b before swapping are = ",a,"  ",b)
a,b = b,a
print("Swapped Values of a and b are =", a,"   ",b)


# Strings
s = "My name is XYZ"
#print the normal string
print(s)
#Printing the string in reversed order
print(s[::-1])


# Using Format Specifiers
name = "David"
age = 23
#O/P - David is 23 years old.
#1st way
print(name," is ",age," years old")
#2nd way
print("%s is %d years old" %(name,age))