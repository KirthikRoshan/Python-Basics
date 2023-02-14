# -*- coding: utf-8 -*-
"""
@author: bstarly

Read Section 1 Chapter 5 (FUNCTIONS) before attempting these exercises.

"""


# Qn 1 Write a function that simply squares and cubes any number passed to it and returns the value.
#The main program should then print the value to the console screen.
#The main program should also 'unpack' the tuple and print its contents.

def squareNcube(num):
    Sq = num*num
    cube = num*num*num
    return (Sq, cube)

num1 = float(input("enter the no: "))
square, Cub = squareNcube(num1)

print(square)
print(Cub)

Sqa = squareNcube(num1)

print(Sqa)


#Qn 2 Write a function that counts the number of even numbers within a list defined by the user. 
#The user enters the numbers on the console, with a comma to separate the numbers. 
#Report the total number of even numbers to the console screen. Example
#Input Enter the numbers (separated by a comma): 1,3,4,6,10,11,12
#Output There are 4 even numbers in the list

def cleanlist(NumList):
    cleaned = [int(num) for num in NumList]
    return cleaned

def countEven(NumList):
    evenList = [num for num in NumList if num%2 == 0]
    return evenList

numListStr = input("enter the numbers:  ")
NumList = numListStr.split(",")

CleeanList = cleanlist(NumList)
print(CleeanList)

evenList = countEven(CleeanList)
print(evenList)



#Qn3
#Write a function that accepts any unspecified number of arguments
#Iterate through the list of arguments. If nothing is passed, handle it approriately
#with an msg displayed back to the user

def hungry(*args):
    if len(args) == 0:
        print("i'm hungry")
    else :
        print("i had ", args)
        
       
        
        
#Main code        
hungry()
hungry("choco")        
hungry("choco", "chips", "3") 










#Qn4
#Write a function that takes the length and breadth of a rectangle of a rectangle.
#Return both the area and perimeter of the rectangle. Also Return back 
#if it is a rectangle or a square.

def SHApe(length,breath):
    if (length==breath):
        shape = "square"
    else:
        shape = "rectangle"

    peri = 2* (length+breath)
    area = length*breath
    
    return peri, area, shape

l = int(input("enter the no:"))

b = int(input("enter the no:"))

shape, perimeter, areas = SHApe(float(l), float(b))

print(areas)
print(shape)
print(perimeter)


#Qn5 
#Write a function that finds the maximum value of all the even numbers in a given list of integers.


def cleanlist(NumList):
    cleaned = [int(num) for num in NumList]
    return cleaned

def countEven(NumList):
    evenList = [num for num in NumList if num%2 == 0]
    return (evenList)

numListStr = input("enter the numbers:  ")
NumList = numListStr.split(",")

CleeanList = cleanlist(NumList)
print(CleeanList)

evenList = countEven(CleeanList)
print(max(evenList))


#Qn6
#Given the dictionary below:
#studentScores={"Bin":[34,43,10], "Johanna":[33,22,77], "Evan":[66,21,97], "Ben":[100,5,10], "Aria":[100,5,10]}
#The values represents a list with scores for 3 exams = Exam 1, Exam 2 and Exam 3 for each student
#A: Check if anyone has scored a 100. Return True, else False
#B: Print all students who scored more than 50 in the 3rd exam


def check100(studentRecords):
    for name, scores in studentRecords.items():
        for score in scores:
            if score == 100:
                return True

    return False


def check50(studentRecords):
    names = []
    for name, scores in studentRecords.items():
        for score in scores:
            if score > 50:
                names.append(name)  #name = key
                
    return set(names)                
            
        
        
        
        
        
studentScores={"Bin":[34,43,10], "Johanna":[33,22,77], "Evan":[66,21,97], "Ben":[100,5,10], "Aria":[100,5,10]}

ret = check100(studentScores)

names = check50(studentScores)

print(ret)
print(names)

#Qn7
#Write a Python program to get a list of dates between two dates 
#entered by the user in mm-dd-yyyy format. Check if the first date is less than second date.
#If the second date is None - then assume it to be today's date or system date.
#The function can have 2 arguments passed to it. The start date being required.
#if the 2nd argument is not passed, then the system's current date must be taken in.

from datetime import date, datetime, timedelta


first = input("enter the 1st date:")
second = input("enter the 2nd date:")

FirstDt = datetime.strptime(first, '%m-%d-%Y')

if second:
    SecondDt = datetime.strptime(second, '%m-%d-%Y')
else:
    SecondDt = datetime.today()
if FirstDt < SecondDt:
    print("sec is greater")    
print("Difference : "+ str(abs(FirstDt - SecondDt)))
print(FirstDt)
print(SecondDt)
    
    
#Qn8  
#Write a program to get a list of dates between two dates entered by the user
#in mm/dd/yyyy. Check also if the first date is less than the second date.


from datetime import date, datetime, timedelta


first = input("enter the 1st date:")
second = input("enter the 2nd date:")

FirstDt = datetime.strptime(first, '%m/%d/%Y')
SecondDt = datetime.strptime(second, '%m/%d/%Y')
 
if FirstDt < SecondDt:
    diff = SecondDt - FirstDt
    print(diff)
    
    for i in range(0, diff.dasy+1):
        print(FirstDt + timedelta(i))
    
    
else:
    print("enter correct data")







   
