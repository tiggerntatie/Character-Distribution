"""
distribution.py
Author: Anoushka Alavilli
Credit: Sarah, Dina, Jasmine, Mr. Dennison, my dad, http://stackoverflow.com/questions/15536287/stripping-commas-and-periods

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
text = input("Please enter a string of text (the bigger the better): ")
text1=text.lower()
strtext= (str(text))
strtext = strtext.replace(",", "")
strtext = strtext.replace(".", "")
strtext = strtext.replace("/", "")
strtext = strtext.replace(":", "")
strtext = strtext.replace("-", "")
strtext = strtext.replace(";", "")
strtext = strtext.replace("'", "")
strtext = strtext.replace('''"''', '''''')
print ('''The distribution of characters in "''' + (strtext) + '''" is: ''')
alphabet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
listnum= []
for i in (alphabet):
    count= (strtext).count(i)
    if (count)>0:
        alphaorder=((i)*(count))
        alphaorderwithnumbers= ((count), (alphaorder))
        listnum.append(alphaorderwithnumbers)
listnum.sort(reverse=True)
#print (listnum)
#print ("")
listnumcount= (len(listnum))
biggestnum= (listnum[0][0])

for i in range ((listnum[0][0]), 0, -1):
    emptylist= []
    for x in (listnum):
        if i==x[0]:
            emptylist.append(x)
    #print ("emptylist =", emptylist)
    if (len(emptylist))>0: 
        emptylist.sort()
        #print ("sortedemptylidt=", sortedemptylist)
        for v in emptylist:
            print (v[1])
        
        
        
