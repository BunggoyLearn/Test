ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)

counts = dict()
names = ['csev', 'cwen' ,'csev' ,'zqian' ,'cwen']
for name in names :
    if name not in counts:
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)
#This loop takes in all the words from a file and counts them based on the words it has in its own dictionary
#If there is a word that is not in the dictionary, it will create a call for that word and start a counter of its own

counts.get(name, 0)
#This function will call for a name and report back the value
#If it isn't there, instead of giving a traceback it will just return the value of 0


counts2 = dict()
names2 = ['csev' , 'cwen' ,'csev' ,'zqian' ,'cwen']
for name2 in names2 :
    counts2[name2] = counts2.get(name, 0) + 1
    print(counts)