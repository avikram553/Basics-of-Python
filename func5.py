mycode = 'print("hello world")'
code = """
def mutiply(x,y):
    return x*y

print('Multiplication of 2 and 3 is: ',mutiply(2,3))
"""
exec(mycode)
exec(code)