"""
distribution.py
Author: <your name here>
Credit: <list sources used, if any>

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
text= input("Please enter a string of text (the bigger the better): ")
text1=text.lower()
strtext= (str(text))
for i in (strtext):
    if ((str(text)).count((i)))>0:
        number=(int((str(text)).count((i))))
        print (number)

#print ('The distribution of characters in "'  + (str(text)) + '" is: ')
#mylist= []
#alphabet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#numbers= ['1','2','3','4','5','6','7','8','9','10','11','12','13',' 14','15','16','17','18','19','20','21','22','23','24','25','26']
#letters= []
#i= letters[-1]
#for x in (strtext):
    #letters[+1]=(x)
    #print (letters)
   
   
   
   
    #if ((str(text)).count((i)))>0:
        #number=(int((str(text)).count((i))))
        #intnumber= int((str(text)).count((i)))
        #letternumberset= ((number), (i))
        #numbers[x]= letternumberset
#print ((i)*(number))

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        