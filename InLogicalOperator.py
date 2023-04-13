fruit = 'banana'
print('n' in fruit)
print('m' in fruit)
print('nan' in fruit)
if 'a' in fruit:
    print ('Found it!')

word = 'banana'
if word == 'banana':
    print('All right, bananas.')
#if the word is banana this will print the phrase
if word < 'banana':
    print ('Your word' + word + ',comes before banana.')
elif word > 'banana':
    print ('Your word' + word + ',comes after banana')
else:
    print('All right, bananas!')
#This will print something for any word and also sort them
#lower case is regarded higher than upper case so Z is smaller than a
#If sorting something like names make sure the casing is correct so it sorts correctly