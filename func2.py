def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0, "Space":0}
    for c in s: #extended for loop
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           d["Space"]+=1
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])
    print ("No of spaces are=",d["Space"])
string_test('Lets deal With PYthon FunctIOns,,,')
