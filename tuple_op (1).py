#tuples
T=(1,3,4,4,'hi!')
print('tuple T: ',T)

#Indexing
print ('T[0]: ',T[0])

#length of tuple
print ('length of tuple: ',len(T))

#if we not use ',' here it will treat it as a string
print('concatenation: ', T + ('everyone',))

#tuples are immutable
print('Tuple: ',T)
#T.remove('4')  

#slicing
print (T[1:4])
T=(2,3,) + T[1:]
print ('now tuple T is:' , T )
print ('now length of tuple:',len(T))

#methods of tuples
#to know the position of an item
