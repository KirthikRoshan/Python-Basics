# -*- coding: utf-8 -*-
"""
@author: bstarly
"""

'''
Complete Watching Module 1 Python Essentials - 1
  - Data Types (List, Sets, Tuples Dictionaries)
  - Basic Math Functions (Round, Min/Max, Random, Sorted)
before attempting these exercises
'''


'''
Qn 1:
a. Define a list of Names that contain Binil, Rachel, Ethan, Evan, Starly, Sam)
b. Print the length of the list.
c. Print the 3rd item in the list.
d. Print the last item in the list    
e. print the entire list
'''
names = ["Binil" , "Rachel ", "Ethan", "Evan", "Starly", "Sam"]

length = len(names)
print("the length of the list is:", length)
print(f"the length of the list is: {len(names)}")
print("the second name is", names[2])
print("the last name is", names[-1])
print("The names are :", names)
print(*names)


'''
Qn 2:
a. Initiate a new Number list and assign it to be empty.
b. Now append the list with numbers 1,3,5,6,7,8,9,10,11,13,15,17,20
c. Print the number that is in the middle of the list.
d. Print the contents of the list that lies between the 4th and 10th index value
e. Reorder the list to be in the reverse order and print the contents to confirm it.
f. find the maximum value in the list
'''

number=[]
#number.append([1,3,5,6,7,8])
number.extend([1,3,5,6,7,8,9,10,11,13,15,17,20])
print(*number)
x=int((len(number)/2))
print(number[x])
print(number[4:11])
print(max(number))
a = number.reverse()
print(number)




'''
Qn 3:
a.  Initiate the following list chocBrandList=["Mars", "Snickers", "Bounty", "Twix"]
b. print the length of the list
c. copy the contents of this list to a new List called newChocList
d. To the original chocBrandList, add the following String - "Lion Bar"    
e. print the contents of the newChocList. Comment on the results obtained
    
'''
chocBrandList = ["Mars", "Snickers", "Bounty", "Twix"]
print(len(chocBrandList))
newChocList = chocBrandList
#print(newChocList)
chocBrandList.append("Lion Bar")
print(newChocList)
#print(chocBrandList)

'''
we can see that adding things to old list will change the new list
but if we print before changing the old then there won't be any change 
'''



'''
Qn 4:
a. Create a dictionary that captures the following values
'red': a random integer between (1 and 10)
'blue': a random integer between (10 and 30)
'green': a random integer between (31 and 70)
'black': a random integer between (71 and 100)
    
'''
from random import randint
colour ={"Red": randint(1, 10), "blue": randint(10, 30), "green": randint(31, 70), "black": randint(71, 100)}
print(colour)

'''
Qn 5:
a. Define a new dictionary with the months of the year as key, and the value 
   being the corresponding number of days in the month
'''
monthDict = {"jan": 31, "feb": 28, "mar": 31, "april":30, "may":31, "june":30, "july":31, "aug":31, "sep":30, "oct":31, "nov":30, "dec":31}
#monthDict ={"mar": 31}
print(monthDict)



'''
Qn 6:
Instantiate a new Dictionary to be empty
Define this dictionary with the following content
Student Name(Key)     Score 1 (Value)
Binil                   78
Starly                  85
Ethan                   89
Jessica                 95 
Carson                  97

a. print the entire dictionary content
b. print the score of Carson
c. Add a new dictionary item with the following student and score: Daniele, 48
d. prints all the values of the dictionary
'''
score = dict()

score.update({"Binil": 78, "Starly":85, "Ethan":89, "Jessica":95, "Carson":97})

print(score)
print(score["Binil"])
score['Daniele']= '48'
print(score)

'''
Qn 7
For the same dictionary, to the scores above, add a new Score 2 for each student.
Student Name(Key)     Score 2 (Value)
Binil                   88
Starly                  58
Ethan                   79
Jessica                 85 
Carson                  67
'''
score.update({"Binil": 88, "Starly":58, "Ethan":79, "Jessica":85, "Carson":67})
print(score)



'''
Qn 8:
For the same dictionary above, copy the content to another dictionary.
Changes to one dictionary should not affect the other.
'''
new_dict = dict(score)
print(new_dict)
score["Binil"]=0
print(new_dict)



'''
Qn 9:
a. Define a tuple with variable aTuple to be containing 1, 4, 2, 5
b. Change the value available at the index value 2 of aTuple to 10
c. Can you convert a Tuple to a List? Convert a List to a Tuple
'''
aTuple = (1,4,2,5)
'''
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
'''
aList = list(aTuple)
print(type(aList))
atuple = tuple(aList)
print(type(atuple))


'''
Qn 10: Write a Python script that would encapsulate the following problem statement
into an appropriate Python Data Structure

A bag contains 10 colored balls that are one of (red, blue, green and black)
For each colored ball, a single integer value is associated with it 
that ranges between 1-20.Both the value and the color are unique and will not repeat
within the bag.

'''
from random import randint,choice
#import random
#from random import 
#bag = {randint(0,3): randint(1, 10)}
dict1 = ["red", "blues", "green", "black", "red", "blues", "green", "black", "red", "blues", "green", "black"]
bag= {choice(list(dict1)): randint(1, 20)}
bag[choice(list(dict1))] = randint(1, 20)
bag[choice(list(dict1))] = randint(1, 20)
bag[choice(list(dict1))] = randint(1, 20)
bag[choice(list(dict1))] = randint(1, 20)
bag[choice(list(dict1))] = randint(1, 20)
bag[choice(list(dict1))] = randint(1, 20)
print(bag)





