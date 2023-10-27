counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()

print('Words: ', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)

jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
print(list(jjj))
#We can print dictionaries as a list
print(jjj.keys())
#We can print the names of the listings with .keys()
print(jjj.values())
#We can print the values of the listings with .values()
print(jjj.items())
#We can print both with .items()

for aaa,bbb in jjj.items():
    print(aaa,bbb)
#We can split .items() into keys and values with 2 iteration variables (aaa,bbb)
