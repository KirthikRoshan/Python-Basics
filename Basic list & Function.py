# -*- coding: utf-8 -*-
"""
@author: bstarly
"""
import random 


   
'''
Qn1
Print the key and values within a dictionary
using FOR loops
'''
nam = {1:"a",2:"b"}
for key,value in nam.items():
    print(key,value)
    #print(value,key)



'''
Qn2
Iterate through a list and create a new list that 
contains the square of the values in the original list
using For Loops & List Comprehensions
'''
num = [1,2,3,4,5]
new_num = []

for i in num:
    val = i*i
    new_num.append(val)
print(new_num)

#list comprehension

new_numComp = [i*i for i in num]
print(new_numComp)

'''
Qn3
Assuming the following data structures capture values obtained from a source
itemsN = ["obj1", "obj2", "obj3", "obj4", "obj5"]
locXYZ = [(3.0, 4.0, 2.0), (3.0, 1.0, 2.0), (6.0, 4.0, 2.0), (.6, 8.9, 4.5), (7.6, 9.9, 4.5)]
Write a script that combines this data into a single dictionary
with keys in itemsN, and the corresponding value being the records in locXYZ
'''

itemsN = ["obj1", "obj2", "obj3", "obj4", "obj5"]

locXYZ = [(3.0, 4.0, 2.0), (3.0, 1.0, 2.0), (6.0, 4.0, 2.0), (.6, 8.9, 4.5), (7.6, 9.9, 4.5)]

res = {itemsN[j]: locXYZ[j] for j in range(len(itemsN))}
print(res)

objXYZ={}
for idx, item in enumerate(itemsN):
    objXYZ[item] = locXYZ[idx]
    
print(objXYZ)    

testX ={}
for k,v in zip(itemsN, locXYZ):
    testX[k] = v

print(testX)


    

'''
Qn4
Assuming the following data structures capture values obtained from a source
itemsN = ["obj1", "obj2", "obj3", "obj4", "obj5", "obj6"]
locXYZ = [(3.0, 4.0, 2.0), (3.0, 1.0, 2.0), (6.0, 4.0, 2.0), (.6, 8.9, 4.5), (7.6, 9.9, 4.5)]
Write a script that combines this data into a single dictionary
with keys in itemsN, and the corresponding value being the records in locXYZ
'''    
itemsN = ["obj1", "obj2", "obj3", "obj4", "obj5", "obj6"]
locXYZ = [(3.0, 4.0, 2.0), (3.0, 1.0, 2.0), (6.0, 4.0, 2.0), (.6, 8.9, 4.5), (7.6, 9.9, 4.5)]

testXa ={}
for k,v in zip(itemsN, locXYZ):
    testXa[k] = v

print(testXa)

#doesn't work

objXYZa={}
for idx, item in enumerate(itemsN):
    objXYZa[item] = locXYZ[idx]
    
print(objXYZa) 

#to make it work
itemsN = ["obj1", "obj2", "obj3", "obj4", "obj5", "obj6"]
locXYZ = [(3.0, 4.0, 2.0), (3.0, 1.0, 2.0), (6.0, 4.0, 2.0), (.6, 8.9, 4.5), (7.6, 9.9, 4.5)]
objXYZab={}
for idx, item in enumerate(itemsN):
    try:
        objXYZab[item]=locXYZ[idx]
    except:    
    
        objXYZab[item] = "error"
       
print(objXYZab)
   
   
   
'''
Qn 5:
Square the values in this list except numbers divible by 5
using List Comprehensions
Given listN=[3,5,6,10,2,3,5]
'''
listN=[3,5,6,10,2,3,5]
SqNon5List=[num*num for num in listN if num % 5 !=0 ]
print(SqNon5List)











'''
Qn6
6.	A user has two standard dices. Each dice has values from 1 through 6. 
The user throws each set of 2 dices 30 times. Simulate this action using a Python script.
Your script must store the value on each dice that appears for each throw. 
a) After 30 throws are completed, find the total sum of the scores obtained by both dices across the 30 throws. 
b) Repeat the simulation of 30 throws, 10 times, record the total Sum obtained each time in a list.
'''

AllTenSum=[]

for tenSim in range(10):
    totalSum = 0
    dlist=[]
    for throw in range(30):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        totalSum = totalSum + dice1 + dice2
        dlist.append((dice1,dice2))
         
    AllTenSum.append(totalSum)
    print(dlist)
    print(totalSum)        
print(AllTenSum)
        
        
        
        
        
        
        
    





