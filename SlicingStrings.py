s = 'Monty Python'
print (s[0:4])
#slicing uses a colon and takes the parts of the string everything between position a to position b including a BUT NOT B
#[a:b] UP TO B but not B
print (s[6:7])
#can slice only one position
print (s[6:20])
#can slice over count without getting a traceback

print (s[:2])
#We can leave out digit a if we want it to start at the beginning
print (s[8:])
#we can also do this with the ending
print(s[:])
#We can do both at the same time and it will just print the whole string
