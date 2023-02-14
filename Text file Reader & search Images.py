# -*- coding: utf-8 -*-
"""
@author: bstarly
"""

    
'''
Qn1
#Write a Program to Write The Given Strings to a File
#n1='\n'
#lines = 'Binil', n1, 'Starly', 'is', n1, 'teaching', n1, 'Python', n1, 'today'

'''
n1='\n'
lines = 'Binil', n1, 'Starly', n1, 'is', n1, 'teaching', n1, 'Python', n1, 'today', n1

file = open("mine.txt", "a")
file.writelines(lines)
file.close()

with open("mine.txt", 'r', encoding="utf-8") as rfile:
    lines = rfile.readlines()
    for line in lines:
        print(line, end="")





'''
Qn2
#Write a function CodeWord(filename) that reads a file ‘CNCFile.txt’ containing a large amount of text.
#For every instance of the word – CNC contained in the file, replace this word with the word – ‘XYZ’. Output this new text to another file – “CodedText.txt”.
#Also output the number of times the word – CNC appeared in the file to the console screen.
'''

rfile = open(r"Data/CNCfile.txt", 'r', encoding=("utf-8"))
ofile = open(r"Data/XVZfile.txt", 'w', encoding=("utf-8"))
wordlist = []
for line in rfile:
    BagOfWords = line.split(" ")
    #print(words)
    
    for word in BagOfWords:
        if 'CNC' in word.upper():  #if "CNC" == word
            word = "XYZ"

        wordlist.append(word)

print(wordlist)

for word in wordlist:
    ofile.write(word+' ')

ofile.close()


'''
QN3:
A: Read the contents (names of the files) of a folder that contains files and sub-folders
B: Calculate the number of JPEG and JSON type files contained. No other file types to be read.
C: Print the file sizes of only the JPEG files contained in the folder
'''

import os
import zipfile as zp

zpName = "Qn3_Data_Content.zip"
zpfile = zp.ZipFile(zpName, 'r')

zpfile.extractall("MetaData/")



#2nd


path = r"MetaData/JSON"
jsonfilelist = [jsonfile for jsonfile in os.listdir(path) if jsonfile.endswith('.json')]
print("no of json", len(jsonfilelist))



path = r"MetaData/JPEG"
#will not go through all file "subfolder"
jpgfilelist = [jpgfile for jpgfile in os.listdir(path) if jpgfile.endswith('.jpg')]
print("no of jpg",len(jpgfilelist))


def getFileSize(path):
    fileNames = []
    filesizes = []
    
    for root, dirs, files, in os.walk(path):
        for file in files:
            if '.jpg' in file:
                fSize = os.path.getsize(os.path.join(root,file))
                fileNames.append(file)
                filesizes.append(fSize/1024)
                
              
            else:
                pass                

    return fileNames, filesizes


fileNames, filesizes = getFileSize(path)
print(filesizes)                

'''
Qn4:
A: Read the contents of all the JSON files within the sample folder.
B: Read all of the volume values inside each of the json files.
C: Report on the total volume by summing all of these values.
'''
import json

#Find the size of all the JPEGs contained in the given folder-sub-folder
def getVolInfo(path, jsonNameList):
    totalVol = 0
    for name in jsonNameList:
        with open(path+name, 'r') as jsonFile:
            dataObj = json.load(jsonFile)
            totalVol = totalVol +  dataObj['volume']
    return totalVol

path=r"MetaData/JSON/"
jsonNameList = [jsonfilelist for jsonfilelist in os.listdir(path) if jsonfilelist.endswith('.json')]

totalVol = getVolInfo(path, jsonNameList)
print("The total volume summed up across all JSON files is:", totalVol)



'''
#Qn5
A: Extract the content of the zip file.
B: Count the number of units sold
C: Find the country that obtained the maximum revenue
D: Output a JSON file that lists each Item_Type and the countries that sold those items
   as a dictionary, in the following format 
   ItemType: List of countries that sold that item 
'''
import zipfile as zp
import csv
import json

path = "5000-Sales-Records.zip"
ourDirName = "Sales_Data//"
zipfile = zp.ZipFile(path, 'r')
fileList = zipfile.namelist() #contains the name of the files in the zip

zipfile.extract(fileList[0], ourDirName)

unitsold=0
with open(ourDirName+ str(fileList[0])) as file:
    content = csv.reader(file)
    next(content)
    for row in content:
        unitsold = unitsold + int(row[8])

print("Total units sold =${:,}".format(unitsold))

#which Country had the highest revenue
maxRev=0
with open(ourDirName+ str(fileList[0])) as file:
    content = csv.reader(file)
    next(content)
    for row in content:
        rev = float(row[11])
        if maxRev < rev:
            maxRev = rev
            maxCountry = row[1]

print("Max Revenue ${:,} was obtained by {}".format(maxRev, maxCountry))

#D
itemTypeDict={}
with open(ourDirName+ str(fileList[0])) as file:
    content = csv.reader(file)
    next(content)
    
    for row in content:
        if row[2] not in itemTypeDict.keys():
            itemTypeDict[row[2]] = [row[1]]
        else:
            itemTypeDict[row[2]].append(row[1])
    

with open(ourDirName+"outputfile.json", 'w') as outfile:
    json.dump(itemTypeDict, outfile)
    

