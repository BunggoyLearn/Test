x = ('Glenn', 'Sally', 'Joseph')
#Tuples are like lists, they have elements which are indexed starting at 0
print(x[2])
y = (1, 9, 2)
print(y)
print(max(y))

for iter in y:
    print (iter)

z = [9, 8, 7]
print(z)
z[2] = 6
print(z)

#z = 'ABC'
#z[2] = 'D'

#z = (5, 4, 3)
#z[2] = 0

#Tuples are immutable which means that if we were to try and change them like strings they would send a traceback

#Tuples are memory efficient, because they are immutable

(x,y) = (4, 'fred')
print(x)
print(y)

#Tuples can be on the left side of assignment statements

print((0, 1, 2) < (5, 1, 2))
print((0, 1, 20000) < (0, 3, 4))
#Both of these statements are true because it works sequentially
#It stops when it finds the first example

d = {'a':10, 'b':1, 'c':22}
print(d.items())

print(sorted(d.items()))
#This will sort the items by the keys rather than the values attached

for k,v in sorted(d.items()):
    print(k, v)
#This allows us to loop through dictionary in key order

tmp = list()
for k,v in d.items():
    tmp.append( (v,k) )

print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)
#We can also sort by values by reversing the search

