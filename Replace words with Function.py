# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 17:26:08 2023

@author: KirthikRoshan
"""

matrix=[    ['VINE', 'THE', 'WONDER', 'PIZZA'],
            ['BEAUTY', 'SIRE', 'NUN','NONE'],
            ['COOPERATION','EAST','NOBODY','OF'],
            ['NOON','OOLONG','THE','UNIVERSE'],
            ['AIRPLANE','MY','SUBTERFUGE','DEED'],
            ['NEVER','WORLD','RESIN','DONOR'],
            ['TOO', 'TWO','CLOUD','EVEN'],
            ['LIES','SERENDIPITY','PRIZE','SWIFT'],
            ['RAPID','OBOE','ANYBODY','IN'],
            ['THE', 'MULTITUDE','SPEEDY','MATHEMATICAL'],
            ['PIZZAZ','SURE','DIVERSITY','RUIN'],
            ['RAINBOW','WARE', 'WEAR','MOON'],
            ['SOMEONE', 'OF', 'STAR','ABBA'],
            ['KAYAK','MONOPOLY','ITS','EYE']
        ]


def New_Text(words, targets, replacements):
    if words == targets:
        return replacements
    return words

def If_they_Have(words, letters):
    return letters in words

def IF_Have_two_or_more_o(words):
    return words.count("O") >= 2 or words.count("o") >= 2

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        words = matrix[i][j]
        
        if j > 0 and matrix[i][j-1] == "THE":
            matrix[i][j] = "NONE"
        elif j == 1 or j == 3:
            if IF_Have_two_or_more_o(words):
                matrix[i][j] = "NONE"
        elif j == 0 or j == 2:
            if If_they_Have(words, "E") or If_they_Have(words, "e"):
                matrix[i][j] = "NONE"

for rows in matrix:
    print(rows)
