def calculateSquare(n):
    return n*n

numbers = (10,2,3,4,5)
result=list(map(calculateSquare, numbers))
print(result)
# converting map object to set
numbersSquare = set(result)
print(numbersSquare)
