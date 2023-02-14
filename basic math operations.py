# -*- coding: utf-8 -*-
"""
@author: bstarly
"""

'''
Qn1
Combine the following lists to a single list
x = [1,5,7,2]
y = [7,3,3,1,6,21,5,22,11]

'''
x = [1,5,7,2]
y = [7,3,3,1,6,21,5,22,11]
z = x + y

print(z)



'''
Qn 2 Write a script that asks the user for three numbers. Each time the user 
inputs the number, convert the input value to an integer using the floor() method. 
Each integer must be appended to a list. For example:

Enter the value: 34.2
Enter the value: 20.0
Enter the value: 1

The list contains 34,20,1
'''
import math
aa = float(input())
ba = float(input())
ca = float(input())
d = math.floor(aa)
e = math.floor(ba)
f = math.floor(ca)
num_list = []
num_list.append(d)
num_list.append(e)
num_list.append(f)
print(*num_list)


'''
Qn2
Take 2 unequal list and create a new list that 
contains only numbers common to both lists
a=[1, 5, 2, 5, 33, 10, 2]
b=[50, 20, 1, 4, 22, 11, 3, 6, 50, 20, 10, 3, 55]

'''
a=[1, 5, 2, 5, 33, 10, 2]
b=[50, 20, 1, 4, 22, 11, 3, 6, 50, 20, 10, 3, 55]

cc = []
cc.append(set(a)&set(b))
print(cc)
'''
Qn3
# Count how many times the word 'and' appears in this paragraph.
# Break the paragraph into individual bag of words
# print total number of individual words in the paragraph
# Break the paragraph into sentences separated by the full stop
# print number of whole sentences in this new broken up list
paragraph = "Walk into the Library this week"+" and you’ll be greeted not by the towering Bookstacks but by soft,"+
            " hanging lights and a grand, open staircase. Faculty offices"+
            " so small they weren’t accessible have been removed, and long"+
            " windows looking out onto campus are now dotted along the walls."+
            " Colorful chairs and wide tables are still spread across the"+
            " floors, but the library is brighter, more spacious and more"+
            " welcoming after a yearlong renovation."
'''
paragraph = ("Walk into the Library this week"+" and you’ll be greeted not by the towering Bookstacks but by soft,"+
            " hanging lights and a grand, open staircase. Faculty offices"+
            " so small they weren’t accessible have been removed, and long"+
            " windows looking out onto campus are now dotted along the walls."+
            " Colorful chairs and wide tables are still spread across the"+
            " floors, but the library is brighter, more spacious and more"+
            " welcoming after a yearlong renovation.")
    
print(paragraph.count('and'))
zz = []
zz = paragraph.rsplit()

print(zz)

print(len(zz))

yy = paragraph.split(".")
print(yy)
print(len(yy))

'''

Qn4
Find Movies that start with a letter G 
movies= ["Star Wars", "Batman", "Gone with the Wind", "Shawshank Redemption"]
Randomly Select 1 movie from the list and check if it starts
with "G".
Print True or False for the above check
Do not use loops or Conditional statements
'''
import random
###filter
movies= ["Star Wars", "Batman", "Gone with the Wind", "Shawshank Redemption"]
print(movies[0][1])

string = "G"
FindStartG = list(filter(lambda x: x[0].lower() == string.lower(), movies))
print(FindStartG)
ee = random.choice(movies).startswith("G")
print(ee)


'''
Qn5
Generate a Ball List which should contain 5 colored balls 
each with an associated integer value.
The Ball List is colored to have exactly 5 Red and 5 Blue Balls.
Each colored ball has a randomly selected score value
between 1 and 20

Print the Original Ball List
Randomly Sample 5 balls from this ball List.
Print the total value of the scores on each of the 5 sampled Balls.
DO NOT USE FOR-LOOPS
'''
from random import choice,randint

ball_list = ["red"]*5 + ["blues"]*5
'''bag_ball_list= {choice(list(ball_list)): randint(1, 20)}
bag_ball_list[choice(list(ball_list))] = randint(1, 20)
bag_ball_list[choice(list(ball_list))] = randint(1, 20)
bag_ball_list[choice(list(ball_list))] = randint(1, 20)
bag_ball_list[choice(list(ball_list))] = randint(1, 20)
'''
# print(ball_list)
bag_ball_list= [{("red"): randint(1, 20)}]
bag_ball_list.append({("red"): randint(1, 20)})
bag_ball_list.append({("red"): randint(1, 20)})
bag_ball_list.append({("red"): randint(1, 20)})
bag_ball_list.append({("red"): randint(1, 20)})
bag_ball_list.append({("blue"): randint(1, 20)})
bag_ball_list.append({("blue"): randint(1, 20)})
bag_ball_list.append({("blue"): randint(1, 20)})
bag_ball_list.append({("blue"): randint(1, 20)})
bag_ball_list.append({("blue"): randint(1, 20)})
print(bag_ball_list)

five_ball_list = random.sample(bag_ball_list,5)

print(five_ball_list)
test0 = list(five_ball_list[0].values())[0]
test1 = list(five_ball_list[1].values())[0]
test2 = list(five_ball_list[2].values())[0]
test3 = list(five_ball_list[3].values())[0]
test4 = list(five_ball_list[4].values())[0]

print(test0+test1+test2+test3+test4)
#result = int(five_ball_list[0].values()) +int(five_ball_list[1].values())+int(five_ball_list[2].values())+int(five_ball_list[3].values())+int(five_ball_list[4].values());
#print( (*five_ball_list[0].values()) + (*five_ball_list[1].values()) + (*five_ball_list[2].values()) + (*five_ball_list[3].values()) + (*five_ball_list[4].values()) )
#print(result)
'''
Qn 6
A user has two standard dices. Each dice has faces values from 1 through 6. 
The user throws each set of two dices 3 times. Simulate this action using a Python script. 
For the three throws, print the total sum of the scores obtained. (Do not use For Loops).

For ex.
Throw 1: 3, 5
Throw 2: 3, 1
Throw 3: 6, 6
Total: 24

'''

from random import choice,randint
dice_list = ["d1"]*3 + ["d2"]*3

bag_dice_list = [{('d1'): randint(1, 6)}]
bag_dice_list.append({('d2'): randint(1, 6)})
bag_dice_list.append({('d1'): randint(1, 6)})
bag_dice_list.append({('d2'): randint(1, 6)})
bag_dice_list.append({('d1'): randint(1, 6)})
bag_dice_list.append({('d2'): randint(1, 6)})

print(bag_dice_list)

xtest0 = list(bag_dice_list[0].values())[0]
xtest1 = list(bag_dice_list[1].values())[0]
xtest2 = list(bag_dice_list[2].values())[0]
xtest3 = list(bag_dice_list[3].values())[0]
xtest4 = list(bag_dice_list[4].values())[0]
xtest5 = list(bag_dice_list[5].values())[0]

print(xtest0+xtest1+xtest2+xtest3+xtest4+xtest5)

'''
Qn 7
For any given list containing a mix of integers and float values, find the sum, 
min and max of values within the list. Delete the minimum value from the original 
list to create a new list. Please note that your solution must work on any length 
of list and that the original list should remain unchanged. Assume that only unique 
values exist within the given list. For example, a sample solution might look like this:
Given List:
A = [10, 0.1, 20.0, 11, 12.3, 30, 23, 33]
Sum: 139.4
Min: 0.1
Max: 33

Original List, A is: [10, 0.1, 20.0, 11, 12.3, 30, 23, 33]
New List, B is: [10, 20.0, 11, 12.3, 30, 23, 33]

'''


list1=[]

for i in range(5):

    a12 = eval(input('enter the number:' ))

    list1.append(a12)

print(list1)

sum_list1 = sum(list1)
print(sum_list1)
print(min(list1))
abc = min(list1)
print(max(list1))

new_list1 = list1.remove(min(list1))

print(list1)


'''
Qn 8
Write a program to define a dictionary object with the following table that 
describes the first names of the students and their corresponding scores for 
Exams 1 and Exam 2. Using the dictionary object, 
print the score associated with Exam 2 of the student – ‘Evan’.

Name	Exam 1	Exam 2
Binil	 83	     100
Starly	100	     93
Ethan	99	     93
Evan	19	     34

'''        

#First_Name = {"name" : ["Binil","Starly","Ethan","Evan"]}
#Exam1 = {"Exam 1" : [83, 100, 99, 19]} 
#Exam2 = {"Exam 2" : [100, 93, 93, 34]}       
        
#print(First_Name)
#print(Exam1)        
#print(Exam2)          
        
#print(First_Name.get('name')[3], "score of exam 2 is",Exam2.get('Exam 2')[3] )
        
Binil = {"name":"Binil", "Exam 1":"83", "Exam 2":"100"}
Starly = {"name":"Starly", "Exam 1":"100", "Exam 2":"93"}      
Ethan = {"name":"Ethan", "Exam 1":"99", "Exam 2":"93"}
Evan = {"name":"Evan", "Exam 1":"19", "Exam 2":"34"}   

print("The score of", Evan.get("name"), "in the exam 2 is",Evan.get("Exam 2"))



