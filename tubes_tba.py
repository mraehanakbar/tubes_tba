#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:37:35 2019

@author: john_wick
"""
inputan = input("masukkan inputan: ")
token = []
valid = "valid"
for i in range (0,len(inputan)):
    skor = 0
    try:
        if(inputan[i] == 'i' and inputan[i+1] == 'f' and inputan[i+2] == 'f' and inputan[i+3] == '') or (inputan[i] == 'I' and inputan[i+1] == 'F'):
            token.append(8)
            skor += 1
        elif (inputan[i] == 'f' and inputan[i-1] == 'i' and inputan[i+1] == 'f') or (inputan[i] == 'F' and inputan[i-1] == 'I' and inputan[i+1] == 'F') :
            skor+=1
        elif (inputan[i] == 'f' and inputan[i-1] == 'f' and inputan[i-2] == 'i') or (inputan[i] == 'F' and inputan[i-1] == 'F' and inputan[i-2] == 'I') :
            skor+=1
        elif ( inputan[i] == 'i' and inputan[i+1] == 'f' and ( (inputan[i+2] == ' ') or (inputan[i+2] == '(') or (inputan[i+2] == ')')  ) ) or ( inputan[i] == 'I' and inputan[i+1] == 'F' and ( (inputan[i+2] == ' ') or (inputan[i+2] == '(') or (inputan[i+2] == ')')  ) ):
            token.append(6)
            skor += 1
        elif ( inputan[i] == 'f' and inputan[i-1] == 'i' and ( (inputan[i+1] == ' ') or (inputan[i+1] == '(') or (inputan[i+1] == ')')  ) ) or ( inputan[i] == 'F' and inputan[i-1] == 'I' and ( (inputan[i+1] == ' ') or (inputan[i+1] == '(') or (inputan[i+1] == ')')  ) ):
            skor += 1
    except:
         if(inputan[i] == 'i' and inputan[i+1] == 'f') or (inputan[i] == 'I' and inputan[i+1] == 'F'):
            token.append(6)
            skor+=1
         if(inputan[i] == 'f' and inputan[i-1] == 'i') or (inputan[i] == 'F' and inputan[i-1] == 'I'):
            skor+=1
    try:
        if (inputan[i] == 'n' and inputan[i+1] == 'o' and inputan[i+2] == 't') or (inputan[i] == 'N' and inputan[i+1] == 'O' and inputan[i+2] == 'T'):
            token.append(2)
            skor += 1
        elif (inputan[i-1] == 'n' and inputan[i] == 'o' and inputan[i+1] == 't') or (inputan[i-1] == 'N' and inputan[i] == 'O' and inputan[i+1] == 'T'):
            skor += 1
        elif (inputan[i-2] == 'n' and inputan[i-1] == 'o' and inputan[i] == 't') or (inputan[i-2] == 'N' and inputan[i-1] == 'O' and inputan[i] == 'T'):
            skor += 1
    except:
        pass
    
    try:
        if (inputan[i] == 'a' and inputan[i+1]=='n' and inputan[i+2] == 'd') or (inputan[i] == 'A' and inputan[i+1]=='N' and inputan[i+2] == 'D'):
            token.append(3)
            skor += 1
        elif (inputan[i-1] == 'a' and inputan[i]=='n' and inputan[i+1] == 'd') or (inputan[i-1] == 'A' and inputan[i]=='N' and inputan[i+1] == 'D'):
            skor += 1
        elif (inputan[i-2] == 'a' and inputan[i-1]=='n' and inputan[i] == 'd') or (inputan[i-2] == 'A' and inputan[i-1]=='N' and inputan[i] == 'D'):
            skor += 1
    except:
        pass
    
    try:
        if (inputan[i-1] != 'x' and inputan[i] == 'o' and inputan[i+1]=='r') or (inputan[i-1] != 'X' and inputan[i] == 'O' and inputan[i+1]=='R'):
            token.append(4)
            skor += 1
        elif (inputan[i-2] != 'x' and inputan[i-1] == 'o' and inputan[i]=='r') or (inputan[i-2] != 'X' and inputan[i-1] == 'O' and inputan[i]=='R'):
            skor += 1
    except:
        pass
    
    try:
        if (inputan[i] == 'x' and inputan[i+1]=='o' and inputan[i+2] == 'r') or (inputan[i] == 'X' and inputan[i+1]=='O' and inputan[i+2] == 'R'):
            token.append(5)
            skor += 1
        elif (inputan[i-1] == 'x' and inputan[i]=='o' and inputan[i+1] == 'r') or (inputan[i-1] == 'X' and inputan[i]=='O' and inputan[i+1] == 'R'):
            skor += 1
        elif (inputan[i-2] == 'x' and inputan[i-1]=='o' and inputan[i] == 'r') or (inputan[i-2] == 'X' and inputan[i-1]=='O' and inputan[i] == 'R'):
            skor += 1
    except:
        pass
    try:
        if(inputan[i] == 't' and inputan[i+1] == 'h' and inputan[i+2] == 'e' and inputan[i+3] == 'n' ) or (inputan[i] == 'T' and inputan[i+1] == 'H' and inputan[i+2] == 'E' and inputan[i+3] == 'N' ):
            token.append(7)
            skor += 1
        elif(inputan[i-1] == 't' and inputan[i] == 'h' and inputan[i+1] == 'e' and inputan[i+2] == 'n' ) or (inputan[i-1] == 'T' and inputan[i] == 'H' and inputan[i+1] == 'E' and inputan[i+2] == 'N' ):
            skor += 1
        elif(inputan[i-2] == 't' and inputan[i-1] == 'h' and inputan[i] == 'e' and inputan[i+1] == 'n' ) or (inputan[i-2] == 'T' and inputan[i-1] == 'H' and inputan[i] == 'E' and inputan[i+1] == 'N' ):
            skor += 1
        elif(inputan[i-3] == 't' and inputan[i-2] == 'h' and inputan[i-1] == 'e' and inputan[i] == 'n' ) or (inputan[i-3] == 'T' and inputan[i-2] == 'H' and inputan[i-1] == 'E' and inputan[i] == 'N' ):
            skor += 1
    except:
        pass
    
    try:
        if (inputan[i] == '('):
            token.append(9)
            skor += 1
    except:
        pass
    
    try:
        if (inputan[i] == ')'):
            token.append(10)
            skor += 1
    except:
        pass
    
    try:
        if (inputan[i] == 'r') and (inputan[i-1] != 'o') and (inputan[i-1] != 'o' and inputan[i-2] != 'x')  or (inputan[i] == 'R') and (inputan[i-1] != 'o') and (inputan[i-1] != 'o' and inputan[i-2] != 'x'):
            token.append(1)
            skor += 1
    except:
        if (inputan[i] == 'r') or (inputan[i] == 'R'):
            token.append(1)
            skor+=1
    
    try:
        if (inputan[i] == 'p') or (inputan[i] == 'P'):
            token.append(1)
            skor += 1
            
    except:
        pass
    
    try:
        if (inputan[i] == 'q') or (inputan[i] == 'Q'):
            token.append(1)
            skor += 1
    except:
        pass
    
    try:
        if (inputan[i] == 's') or (inputan[i] == 'S'):
            token.append(1)
            skor += 1
    except:
        pass
    
    try:
        if (inputan[i] == '') or (inputan[i] == ' '):
            skor+=1
    except:
        pass
    
    if (skor == 0):
        token.append("error")
        break
    

for j in range(0,len(token)):
    try:
        count_9 = token.count(9)
        count_10 = token.count(10)
        if (token[j] == 1 and token[j+1] == 1) or (count_9 != count_10) or ("error" in token) or ( token[0] == 2 or token[0] == 2 or token[0] == 3 or token[0] == 4 or token[0] == 5 or token[0] == 7 ):
            valid = "not valid"
            break
        else:
            valid = "valid"
    except:
        pass

print(token)
print(valid)
