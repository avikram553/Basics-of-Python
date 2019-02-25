#tuples
T=(1,3,4,4,'hi!')
print ('tuple T: ',T)

#Indexing
print ('T[0]: ',T[0])

#length of tuple
print ('length of tuple: ',len(T))

#if we not use ',' here it will treat it as a string
print ('concatenation: ', T + ('Arka',))

#tuples are immutable
print ('Tuple: ',T)

#slicing
print (T[1:4])
T=(2,3) + T[1:]
print ('now tuple T is:' , T )
print ('now length of tuple:',len(T))

#methods of tuples
#to know the position of an item
print ('positon of hi! in tuple T: ',T.index('hi!'))

#counting the occurence of an item
print ('no of 4 in tuple: ',T.count(4))

#nesting
T = (5,6,[7,8,[12,13]],9,('hi','python'),{'a':'b'})
print ('Tuple: ',T)
T[2][0]=0
print ('Tuple: ',T)
print ('T[2]: ',T[2])
print ('T[2][2]: ',T[2][2])
print ('T[2][2][1]: ',T[2][2][1])

