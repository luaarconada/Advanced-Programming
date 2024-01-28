# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 11:29:39 2023

@author: Usuario
"""
############################# Exercise 1 #############################
#Create string with text
x = "'In a village of La Mancha, the name of which I have no desire to call to mind'"
print(x)

#Convert it to capital letters
up = x.upper()
print(up)

#Revert the text, so it is from end to beginning (using slicing)
rever = up[::-1]
print(rever)

#Obtain another string by keeping one character every 4 characters (using slicing)
four = rever[::4]
print(four)

############################# Exercise 2 #############################
#Marronero
my_list=[[1,2,[3,4]],[5,6]]
my_list[0][2]=[3,3.25,3.75,4]
my_list[0][2]
more_list=[[1,2,my_list[0][2]],[5,6]]
print(more_list)

#Teacher's solution
#We access the first list [1,2,[3,4]], then [3,4] and we change places 1,2,3 with [3.25,3.75,4]
my_list[0][2][1:4]=[3.25,3.75,4]
print(my_list)


############################# Exercise 3 #############################
#Create my dictionary (given)
inventory = {
'gold':500,
'pouch': ['flint', 'twine', 'gemstone'],
'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

#Add a key 'pocket' with value ['seashell','Berry']
inventory['pocket']=['seashell','Berry']
print(inventory)

#Sort the items of key 'backpack'
inventory['backpack'].sort()
print(inventory)

#Remove 'dagger' from 'backpack'
inventory['backpack'].remove('dagger')
print(inventory)

#Add 1 to 'gold' key
inventory['gold']+=1
print(inventory)    
############################# Example mine ###########################
#Let's see if 'potato' is on the basket
basket=set(['orange','apple','apple','banana'])
print(basket)
if('potato' in basket):
    print('noice')
else:
    print('fuck')
    
############################# Exercise 4 #############################
#Compute the unique letters in strings “abracadabra” and “alacazam"
x='abracadabra'
unique=set(x)
print(unique)
y='alacazam'
unique2=set(y)
print(unique2)

#Compute the letters that are in 'abracadabra' but not in 'alacazam
print(unique - unique2)

############################# Exercise 5 #############################
#Create a list of numbers [0,2,3,4,5,6]
x=[0,2,3,4,5,6]
print(x)

#Iterate use a for loop and for each element print 'even' or 'odd'
for i in x:
    if i%2==0:
        print('even')
    else:
        print('odd')
print('The loop is done')

#Try with another list
x=[1,7,3,2,0]

############################# Exercise 6 #############################
x=[0,1,3,4,5,6]
suma=0
for i in x:
    suma = suma + i
print(suma)

############################# Exercise 7 #############################
#Given the stock and price dictionaries:
stock = {'beer': 21, 'olive oil': 2 }
price = {'milk': 1.5, 'beer': 3, 'olive oil': 4}
#Compute the total cost of all the objects in the stock
money=0
for food in stock.keys():
    if food in price.keys():
        money= money + price[food]*stock[food]
print(money)    

############################# Exercise 8 #############################

hobbit_words = 'In a hole in the ground there lived a Hobbit'.lower().split(' ')
print(hobbit_words)
#Use a for loop and a default dictionary to count words in the hobbit_words sentence
from collections import defaultdict
dictionary=defaultdict(lambda:0)
for word in  hobbit_words:
    dictionary[word]+=1
print(dictionary)

#With normal dictionary
dictio={}
for word in hobbit_words:
    if word in dictio:
        dictio[word]+=1
    else:
        dictio[word]=1
print(dictio)

############################# Exercise 9 #############################
#Write a Python function that computes the factorial of a number. If the input
#is negative, print “Error”. If there is no input, the function should compute
#the factorial of zero.

def fact(x=0):
    """Compute the factorial of a number""" #Documentation to know what it does
    if x<0:
        print('Error')
    elif x==0:
        return(1)
    else:
        return(x*fact(x-1))

fact(3)
fact()
fact(0)
#Print the documentation to see what it does
print(fact.__doc__)

############################# Exercise 10 #############################
#Se lo saltó

############################# Exercise 11 #############################
#Use a list comprehension to filter the positive numbers in a list of numbers/
lista=[0,3,-1,4,-3,-4,2]
result=[a for a in lista if (a>0)]
print(result)


#Podría definir una función que me dice si un número es negativo
def pos(x):
    return(x>0)
pos(4)
pos(-3)
pos(0)

result=[a for a in lista if pos(a)]

################ Example of reducing lists without using lambda #############
def sumar(x,y):
    return(x+y)
from functools import reduce
numbers=[2,5,1,6,2]
suma=reduce(sumar,numbers)
print(suma)

############################# Exercise 12 #############################
#Compute the unique words present in three sentences (hint: use reduce and sets)
sentences = ['In a hole in the ground there lived a Hobbit',
'It was the best of times it was the worst of times',
'Somewhere in La Mancha in a place whose name I do not care to remember']

#Create a list of 3 sets that contain the unique words
#We use .split(' ') so they are words and not letters and .lower() so It and it
#aren't considered different words
words=[set(a.lower().split(' ')) for a in sentences]
print(words)

#We join the 3 sets into 1 using the union |
words_join= reduce(lambda x,y:x|y ,words)
print(words_join)

#He says that sets cannot be sorted and list can, but i think it worked with the set

print(sorted(words_join))
print(words_join)
print(sorted(list(words_join)))

############################# Exercise 13 #############################


