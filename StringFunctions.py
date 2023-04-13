greet = 'Hello Bob'
zap = greet.lower()
#turns the string all lowercase
print(zap)
print(greet)

print('Hello Bob'.lower())
#You can also just not define it and use it in the same line
print('Hello Bob'.upper())
#You can also do uppercase
print('Hello Bob'.capitalize())
#You can also just capitalize the first letter of the string


stuff = 'Hello World'
print(type(stuff))
#Finds the type that it is (in this case its STR [STRING])
print(dir(stuff))
#Prints the directory of everything you can do(METHODS) to a string

fruit = 'banana'
pos = fruit.find('na')
print(pos)
#finds the first place that the piece of the string is shown, so the second 'na' is not expressed
pos = fruit.find('aa')
print(pos)
#if there is no position in which the piece of the string is, it will return -1

greet = 'Hello Jimmy'
bcs = greet.replace('Jimmy','Saul')
print(bcs)
#replace replaces part of the string(a) with a new part (b) (a,b)
bcs = greet.replace('m','b')
print(bcs)
#This can be done with individual letters and executed on every part of the string

hello = '                  This will look weird without fixing                 this will still look weird             '
print (hello.lstrip())
#This removes white space from the left of the string
print(hello.rstrip())
#This removes whitespace from the right of the string
print(hello.strip())
#This removes all the white space from both sides, but not from the middle


line = 'My nama Jeff'
print(line.startswith('My'))
#This will report back true because line starts with 'My'
print(line.startswith('m'))
#This will report back false because of the casing issue, it will not flag the 'm' as 'M'


data = 'From android.sitko@gmail.com Fri 4 7 10:10:00 2023'
atsign = data.find('@')
#.find will tell you the position of the string fragment you type in REMEMBER: STRINGS START AT 0
print(atsign)
spaceplace = data.find(' ',atsign)
#You can create a starting and ending point with .find so I can look for ' ' (a) from point atsign (B) and it will
#tell me the nearest white space moving forward and report its position
print(spaceplace)
hostdomain = data[atsign+1 :spaceplace]
#I can now slice the host out easily and get rid of the @ by adding one to the position of atsign
print(hostdomain)