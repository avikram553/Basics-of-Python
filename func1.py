no = 100
def sum(no):
    if no==0:
        return 0
    else:
        return no + sum(no-1)
print("Sum is = ",sum(no))