abc = 'With three words'
stuff = abc.split()
#split breaks strings into parts and produces a list of strings
print(stuff)
print(len(stuff))
print(stuff[0])

for w in stuff :
    print(w)
#This is a simple loop that prints each string on its own line as it moves through

line = 'A lot                     of spaces'
etc = line.split()
print(etc)
#splits will ignore a lot of spaces and still only single out the strings themselves

line2 = 'first;second;third'
thing = line2.split()
print(thing)
print(len(thing))
#Sometimes strings we get back are not spaced with ' ' so it doesn't work

thing2 = line2.split(';')
print(thing2)
print(len(thing2))
#we can set .split(DELIMITER) to whatever and it will use those points as a splitter instead of ' '