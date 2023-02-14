# -*- coding: utf-8 -*-
"""
@author: bstarly
"""

'''
Qn 1 (10 points)
Read the file ‘grades.csv’. Write code that finds and displays the 5 student IDs 
and their corresponding grades who received the lowest grades in the class. 
Some students have not appeared for the exam, but they are not to be treated as 0. 
They need to be simply skipped from the computation. (20points)
'''


"""
Created on Sat Feb  4 17:43:25 2023

@author: KirthikRoshan
"""

import csv
blank = []
with open("./grades.csv", 'r') as file:
  csvreader = csv.reader(file)

  for row in csvreader:
      if row[1] == 'Scores' or row[1] == '':
          pass
      else:
          blank.append(row)

print("\nAll students mark with ID\n",blank)
x = sorted(blank, key= lambda r:int(r[1]), reverse= False)
print("\n5 student IDs and their corresponding grades who received the lowest grades in the class\n",x[:5])


'''
Qn 2 (20 points)
Open and read the contents of the file – ‘2_NoofParts_assem.txt’. Perform the following (20 points):
a)	Calculate how many entries are available in that file excluding the header.
b)	Calculate the sum of all parts from each file. Essentially, finding the sum of all values contained in the 2nd column of the file.
c)	Extract the part ID that has the largest associated no. of parts from the entire list.
'''


"""
Created on Sat Feb  4 19:17:28 2023

@author: KirthikRoshan
"""

import csv
blank = []
#with open(r"2_NoofParts_assem.txt", 'r') as fp:
rfile = open(r"2_NoofParts_assem.txt", 'r', encoding=("utf-16"))

#ofile = open(r"3_NoofParts_assem.txt", 'w', encoding=("utf-16"))
for line in rfile:
    blank.append(line)


x = (len(blank)-1)

print("The Total Number of entries excluding Header:",x)





abc = []
for i in range(1,len(blank)):
    x = blank[i].split('\t')[1]
    if x != '':
        abc.append(int(x))
#print(abc)
kir = abc
print("Sum of No of Parts:",sum(abc))


abcd = []
for i in range(1,len(blank)):
    x = blank[i].split('\t')[2]
    if x != '':
        abcd.append(int(x))
#print(abcd)
print("Sum of Parts Completed",sum(abcd))

abcde = []
for i in range(1,len(blank)):
    x = blank[i].split('\t')[0]
    if x != '':
        abcde.append(x)

#print(max(kir))
max_index = abc.index(max(abc))


print("This is largest associated no. of parts from the entire list",max_index)

print("This is Part ID associated with largest no. of parts from the entire list",abcde[max_index])


'''
Qn 3 (25 points)
Using a python script, open the files contained in the .zip file – “3_Jobs_Completed_log.zip”. 
Scan the files for the line that starts with the word string – “Jobs Completed.. ”.
Extract the number associated with this line and for all instances that this word string appears across all log files,
count the total sum across all files contained within the .zip file. (20points) 

For example:

 	Jobs Completed.. 10 2018-09-04 08:21:28.503153

Extract the number 10 from this sentence which signifies the total number of jobs completed at the point in time.  
Find for all instances in which the string - ‘Jobs Completed’ appears, 
find the total number of jobs completed by adding the numbers from across the provided log files.
'''

"""
Created on Thu Feb  9 14:51:17 2023

@author: KirthikRoshan
"""

import zipfile as zp
import os
zip = zp.ZipFile("K:\\sem2 spring23\\mfg 598 python\\HW3_Files-1\\HW3_Data_Files\\Jobs_Completed_log.zip",'r')
ZipFiles = zip.namelist()
String_Search = "Jobs Completed"
occurences = []

zip.extractall("K:\\sem2 spring23\\mfg 598 python\\HW3_Files-1\\HW3_Data_Files\\Jobs_Completed_log")
path = "K:\\sem2 spring23\\mfg 598 python\\HW3_Files-1\\HW3_Data_Files\\Jobs_Completed_log"
filelist = os.listdir(path)
print(filelist)
for i in range(5):
    print(path+'\\'+ZipFiles[i])
    with open(path+'\\'+ZipFiles[i], 'r') as f:
        file_content = f.readlines(0)
        
        for num,line in enumerate(file_content,0):
            if String_Search in line:
                print(f"\nQ3(a) The line number is {num} and the line is: {line}\n")
                occurences.append(line)

DataSplitFn = [int(i.split()[2]) for i in occurences]

sum_jobs = 0
for i in range(len(DataSplitFn)):
    sum_jobs = sum_jobs + DataSplitFn[i]
print(f"\nQ3(b) The total number of completed jobs across all log files {sum_jobs}\n")


'''
Qn 4 (20 points)
For the same files above, calculate the following:
a)	How many jobs were completed in the period between 15th Aug 2018 to 15th Sept 2018?
b)	The day of the year in which the maximum number of jobs was completed.
c)	Calculate the total number of days elapsed between the time at which the first job batch was completed to the last batch completed.
'''

"""
Created on Thu Feb  9 14:51:17 2023

@author: KirthikRoshan
"""

from datetime import date
from datetime import datetime as dt
import zipfile as zp
import os
zip = zp.ZipFile("K:\\sem2 spring23\\mfg 598 python\\HW3_Files-1\\HW3_Data_Files\\Jobs_Completed_log.zip",'r')
ZipFiles = zip.namelist()
String_Search = "Jobs Completed"
occurences = []
job_sum = {}
zip.extractall("K:\\sem2 spring23\\mfg 598 python\\HW3_Files-1\\HW3_Data_Files\\Jobs_Completed_log")
path = "K:\\sem2 spring23\\mfg 598 python\\HW3_Files-1\\HW3_Data_Files\\Jobs_Completed_log"
filelist = os.listdir(path)
print(filelist)
for i in range(5):
    with open(path+'\\'+ZipFiles[i], 'r') as f:
        file_content = f.readlines(0)
        for num,line in enumerate(file_content,0):
            if String_Search in line:
                occurences.append(line)
DataSplitFn = [i.split() for i in occurences]
date_data = [dt.strptime(i[3],'%Y-%m-%d') for i in DataSplitFn]
for i in DataSplitFn:
    if i[3] in job_sum.keys():
        job_sum[i[3]] = job_sum[i[3]] + int(i[2])
    else:
        job_sum[i[3]] = int(i[2])      
job_comp_sum = 0
fro_date = date(2018,8,15)
to_date = date(2018,9,18)
for i in job_sum.keys():
    if (i>str(fro_date)) & (i<str(to_date)):
        job_comp_sum = job_comp_sum + job_sum[i]
print("\nQ4(a) The total number of jobs completed in the given period is: \n",job_comp_sum)
max_job_date = max(job_sum, key = job_sum.get)
print(f"\nQ4(b) The maximum number of jobs were completed on {max_job_date} which is {job_sum[max_job_date]}\n")
sorted_date_data = sorted(date_data)
time_elapsed = (sorted_date_data[len(sorted_date_data)-1] - sorted_date_data[0]).days
print(f"\nQ4(c) The time elapsed between first job and the last job {time_elapsed} days \n")



'''
Qn 5 (25 points)
Read the following (6_Part1.stl) triangular mesh file available in ASCII format. 
For those of you aware of 3D printing, you will recognize this is as a .STL file. 
For those who aren’t aware of what a .STL file is, please read up online on the format of a .STL ascii file. 
An ASCII formatted .STL file can be opened in any text editor. 
Every vertex of the triangle is preceeded by the word ‘vertex’ followed by the x, y and z coordinates. 
Therefore, ONE Triangle should have 3 vertex entries. Typically, the units is not specified, 
but you can assume it to be in millimeters. 

Write functions that calculate the following: (20 points)
a.	Find the total number of triangles listed in the file.
b.	Store the coordinates of each triangle in a 3-tuple list containing N indices, where N is the total number of triangles.
c.	List the area of each triangle in the file. Compute the total surface area of all triangles listed in the file.
Read up online on the formula to calculate the area of a triangle, given three vertices.
'''

"""
Created on Thu Feb  9 14:51:17 2023

@author: KirthikRoshan
"""

import math
f = open("K:\\sem2 spring23\\mfg 598 python\\HW3_Files-1\\HW3_Data_Files\\6_Part1.stl", 'r')
search_wrd = "vertex"
TriangleVertex = []
TriangleCoordinates = []
TriangleArea = []
VertexofTriangle=[]
for line in f:
    if search_wrd in line:
        TriangleVertex.append(line)
        x = line.split()
        TriangleCoordinates.append((float(x[1]),float(x[2]),float(x[3])))
while(len(TriangleCoordinates)):
    VertexofTriangle.append([TriangleCoordinates.pop(0),TriangleCoordinates.pop(0),TriangleCoordinates.pop(0)])
print("\nQ5(a) Total number of triangles in the file is : ", len(VertexofTriangle))
for i in VertexofTriangle:
    a = ((i[0][0] - i[1][0])**2+(i[0][1] - i[1][1])**2+(i[0][2] - i[1][2])**2)**0.5
    b = ((i[1][0] - i[2][0])**2+(i[1][1] - i[2][1])**2+(i[1][2] - i[2][2])**2)**0.5
    c = ((i[2][0] - i[0][0])**2+(i[2][1] - i[0][1])**2+(i[2][2] - i[0][2])**2)**0.5
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    TriangleArea.append(area)
print("\nQ5(b) The list of tuples containing the coordinates of vertices of each triangle : ",VertexofTriangle)
print("\nQ5(c) The list of area of each triangle is : ", TriangleArea)
print("\nThe total surface area of all the triangles is : ", math.fsum(TriangleArea))
