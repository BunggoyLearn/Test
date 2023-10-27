import re
#To use regular expressions we need to import it

hand = open('items2.txt')
for line in hand:
    line = line.rstrip()
    if line.find('Plasma') >= 0:
        print(line)
#This is the old way of doing it

hand2 = open('items2.txt')
for line2 in hand2:
    line2 = line2.rstrip()
    if re.search('Plasma', line2) :
        print(line2)
#Using re.search() can do the same thing
#re.search() gives us a True/False return if the string matches the expression

hand3 = open('items2.txt')
for line3 in hand3:
    line3 = line3.rstrip()
    if line3.startswith('Plasma'):
        print(line3)
#To write code to look for lines starting with () we would need
#to write something different

hand4 = open('items2.txt')
for line4 in hand4:
    line4 = line4.rstrip()
    if re.search('^Plasma', line4) :
        print(line4)
#We barely have to augment the re.search() function to get the same thing

x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)
#re.findall extracts the matching strings

y = re.findall('[AEIOU]+',x)
print(y)
#This will return nothing because there are no uppercase vowels availiable

g = 'From: Using the : character'
h = re.findall('^F.+:',g)
print(g)
#The multiple spaces characters are greedy and will try to give the largest
#example possible to fit the parameters, making finding From:
#and only From: an issue
h = re.findall('^F.+?:', x)
#Using ? we can make it find the shortest possible which returns what the other would not

a = 'From asitko@ucsd.edu Sat Jun 5 09:14:16 2008'
b = re.findall('\S+@\S+', a)
print(b)
#S+ means atleast one non-whitespace character

b = re.findall('^From (\S+@\S+)',a)
print(b)
#Does same thing but starts with From

hands = open('mbox-short.txt')
numlist = list()
for lines in hands:
    lines = lines.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', lines)
    if len(stuff) !=1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum: ', max(numlist))

#/$
#/ Will make characters that usually do something be searched for rather 
#than do regular expressions
