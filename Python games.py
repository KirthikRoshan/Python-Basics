# -*- coding: utf-8 -*-
"""
@author: bstarly
"""

   
'''
Qn1
Find if the word 'is' exists in the paraph and count how many times
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



print(paragraph.count('is'))

'''
Qn 2
Let’s play Rock, Paper and Scissors. Devise a program that lets the user 
play the game with the Computer for a specified number of attempts. For each attempt, 
the user inputs his/her hand and the computer randomly picks one from the list. 
If you know the game – Rock beats Scissors; Paper beats Rock; Scissors beats Paper. 
The algorithm should also track the score for the user and the Computer until the end of the game.  
A sample I/O is shown as follows:

Input:
Welcome to the Game. My name is “RoPaSc” Gamer
Enter number of attempts: 5
Enter your name: Binil

Input:
Attempt 1: Show your Hand: Rock

Output
Sorry, you lost. Computer picked Paper. 
Score: User: 0; Computer: 1

Input
Attempt 2: Show your Hand: Paper
Output
Sorry, you lost: Computer picked Rock
Score: User: 0; Computer: 2
..
..
(After the 5 attempts are over, the algorithm should display who won the game)

Output:
Congratulations Computer, you won the game! Sorry, Binil, you lost.

Final Score: Binil - 2; Computer - 3

'''


# @author: KirthikRoshan

print("\nWelcome to the Game. My name is “RoPaSc” Gamer\n")
num = int(input("\nEnter number of attempts:\n",))
#print(num)
name = str(input("\nEnter your name:\n",))
#print(name)
user = []
computer = []


  
import random

i = 1
while i < num+1:
  
    
  
    user_action = input("\nShow your Hand (rock, paper, scissors): \n")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\n{name} chose {user_action}, computer chose {computer_action}.\n")
    
    if user_action == computer_action:
        print(f"\nBoth players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print(f"\nRock smashes scissors! {name} win!")
            user.append(1)
        else:
            print(f"\nPaper covers rock! {name} lose.")
            computer.append(1)
         
            
    elif user_action == "paper":
        if computer_action == "rock":
            print(f"\nPaper covers rock! {name} win!")
            user.append(1)
        else:
            print(f"\nScissors cuts paper! {name} lose.")
            computer.append(1)
            
             
    elif user_action == "scissors":
        if computer_action == "paper":
            print(f"\nScissors cuts paper! {name} win!")
            user.append(1)
        else:
            print(f"\nRock smashes scissors! {name} lose.")
            computer.append(1)
    #print(f"\nCur Score: {name} - {len(user)}; Computer - {len(computer)}\n")
    i += 1 
    print(f"\n Round {i-1} Score: {name} - {len(user)}; Computer - {len(computer)}\n")   
   
    
   
#print(f"\nnumber of times {name} won :",len(user))
#print("\nnumber of times computer won :",len(computer))
print(f"\nFinal Score: {name} - {len(user)}; Computer - {len(computer)}\n")
if (len(user) > len(computer)):
    print(f"\nCongratulations {name}, you won the game! Sorry, computer, you lost.")
elif (len(user) == len(computer)):
    print(f"\nCongratulations {name} and computer, you tied the game!.")
else:
    print(f"\nCongratulations Computer, you won the game! Sorry, {name}, you lost.")

        

    
'''
Qn 3 
Erin plays a lottery game called – “Choose a number and win $’, in which the player must first select a number, N and 
she will then be awarded money, M in $ based on the N selected. She is only allowed to choose from 1 to 100. The pattern goes as follows:
N	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	..
M	3	2	1	6	5	4	3	2	1	12	11	10	9	8	7	6	5	4	3	2	1	24	23	22	..

For example, if Erin chooses '12' from the table she gets $10. She has 5 attempts. After the 5th attempt, the game ends.
a.	Write a program that will first generate the dictionary as shown above. Confirm if the dictionary has been generated correctly based on the pattern seen above.
b.	Present a user input choice to allow Erin to enter 5 numbers between 1 and 100. Check if the user inputs are between 1 and 100. If not, ask the user to input again.
c.	Then display the total $ won by Erin based on the 5 input numbers

'''


i = 1
j = 0
k = 2
n = []
m = []
while i < 101:
    if j == 1:
        k = 2
        j = k+i
        
    elif j != 1:
        j = k+i
   
        #print(i,".")
        #print(j,".")
        n.append(i)
        m.append(j)
        i += 1
        k -= 2
        


#print(n)
#print(m)

res = dict(zip(n,m))

print(res)

#f = int(input("\nenter the first number between 1-100\n"))

aaa = list()
count = 0
print("Loop wont close until you enter correct number")

while True:
    val = int(input(f"Enter value of {count+1} between 1 to 100\n")) 
    if val>0 and val<100:
        count = count+1
        aaa.append(val)
    if count ==5:
        break
    

print(aaa,"selected numbers")
'''for i in range(101):
    f = int(input("\nenter the first number between 1-100\n"))
    s = int(input("\nenter the second number between 1-100\n"))
    t = int(input("\nenter the third number between 1-100\n"))
    fo = int(input("\nenter the fourth number between 1-100\n"))
    fi = int(input("\nenter the fifth number between 1-100\n"))


    if (f and s and t and fo and fi) >0 and (f and s and t and fo and fi) <101:
        print("\n correct value \n")
        break
    else:
        print("\n wont stop till correct number\n")'''
'''
#s = int(input("\nenter the second number between 1-100\n"))
for s in range(101):
    s = int(input("\nenter the second number between 1-100\n"))
    if s >0 and s <101:
        print("\n correct value \n")
        break
    else:
        print("\n wont stop till correct number\n")

#t = int(input("\nenter the third number between 1-100\n"))
for t in range(101):
    t = int(input("\nenter the third number between 1-100\n"))
    if t >0 and t <101:
        print("\n correct value \n")
        break
    else:
        print("\n wont stop till correct number\n")

#fo = int(input("\nenter the fourth number between 1-100\n"))
for fo in range(101):
    fo = int(input("\nenter the fourth number between 1-100\n"))
    if fo >0 and fo <101:
        print("\n correct value \n")
        break
    else:
        print("\n wont stop till correct number\n")

#fi = int(input("\nenter the fifth number between 1-100\n"))
for fi in range(101):
    fi = int(input("\nenter the fifth number between 1-100\n"))
    if fi >0 and fi <101:
        print("\n correct value \n")
        break
    else:
        print("\n wont stop till correct number\n")
'''

a = res.get(aaa[0])    
print(a,"\n is the amount won")
b = res.get(aaa[1])
print(b,"\n is the amount won")
c = res.get(aaa[2])
print(c,"\n is the amount won")
d = res.get(aaa[3])
print(d,"\n is the amount won")
e = res.get(aaa[4])
print(e,"\n is the amount won")

add = a+b+c+d+e
print("the total value earned",add)


'''
Qn 4
Write a function that accepts a single argument as a list. 
It should return to the main function a new list that contains only names that have 6 or more characters in them. For example:

Assign 
nameList = [‘Binil’, ’Starly’, ’Ethan’, ‘Evan’, ‘Rachel’, ‘Aria’, ’Claudia’]

Your code should output the following:
longNames = [’Starly’, ‘Rachel’, ‘Claudia’]

'''



input_string = input('Enter elements of a list separated by space ')
print("\n")
user_list = input_string.split()
# print list
print('list: ', user_list)


def sixlenfun():

    nameList = user_list
    longNames = []
    
    max_len = 6
    for ele in nameList: 
        if(len(ele) >= max_len): 
            #max_len = len(ele) 
            #res = ele
            longNames.append(ele)
            #print(maxlist)
            #return
    #print("Longest String is : ", res)
    print(longNames)
    return longNames
sixlenfun()











'''
Qn 5
The future value of money, relates how much a current investment will be worth in the future, assuming a constant interest rate.

FV = PV * (1 + Int)^n
Where FV = future value; PV = Present value; Int = interest rate per compounding period expressed as a fraction, ex 5% as 0.05; n = compounding periods (12)
Write a Python function to calculate FV with the three inputs (PV, Int, n). 
Dr Starly has three options to decide on where to invest $10,000, as given by the table. 
Generate an output that displays the value in his account every year until the maturity year.

Financial Institution	Int. Rate per month	  Min. Years
NC Capital Bank	             4.3%	             6
Mutual funds	             3.6%	             5
Allie Bank	                 2.5%              	 1

'''
"""
Created on Wed Feb  1 12:41:02 2023

@author: KirthikRoshan
"""

NC_Capital_Bank	= {"PV" : "10000","Interest":"4.3","no":"6"}
Mutual_funds	= {"PV" : "10000","Interest":"3.6","no":"5"}
Allie_Bank	= {"PV" : "10000","Interest":"2.5","no":"1"}


def future(**arg1):
    
    PVs = arg1["PV"]
    Ints = arg1["Interest"]
    n = arg1["no"]
    
    PVsa = float(PVs)
    Intsa = float(Ints)
    na = int(n)
    num = 1
    
    for num in range(na+1):
    
        FV = PVsa * ((1+(Intsa/100))**num)
        
        print(FV)
    num += 1
    
    return FV
    
future(**NC_Capital_Bank)

