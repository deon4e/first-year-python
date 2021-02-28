# anagramsearch.py
# By Deon Fourie
# 10 May
import sys
print("***** Anagram Finder *****")

try:
    ew = open("EnglishWords.txt", "r")
    word = str(input("Enter a word: "))    
    lines = ew.readlines()
    s = lines.index("START\n")
    theline = lines[s+1:]
    
    list1 = []
    word = word.lower()
    
    for i in word:
        list1.append(i)
    list1.sort()
    
    list2 = []
    list3 = []
    
    for j in theline:
        if j[len(j)-1:] == '\n':
            m = j.replace("\n", "")
        else:
            m = j
        if m != word:
            for k in m:
                list2.append(k)
                list2.sort()
            if list2 == list1:
                list3.append(m)
                list2 = []      
            else:
                list2 = []    
            
    list3.sort()
    if len(list3) == 0:
        print("Sorry, anagrams of '", word, "' could not be found.", sep='')
    else:
        print(list3)
    ew.close()

except FileNotFoundError as error:
    print("Sorry, could not find file 'EnglishWords.txt'.")
    
    
    




    
    
    



        