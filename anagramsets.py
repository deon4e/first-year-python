# Anagramssets.py
# By Deon Fourie
# 10 May

print("***** Anagram Set Search *****")
length = int(input("Enter word length:\n"))
print("Searching...")
file = str(input("Enter file name:\n"))
print("Writing results...")

f = open("EnglishWords.txt", "r")
lines = f.readlines()
f1 = open(file, "w")
s = lines.index("START\n")
theline = lines[s+1:]

lenoflist = []

for i in theline:
    if len(i)-1 == length:
        lenoflist.append(i[:len(i)-1])
lenoflist.sort()

anagramfinal = []

def anagramfinder(word1):
    list1 = []
    list_word = []
    anagrams = []
    anagrams.append(word1)
    
    for h in word1:
        list1.append(h)
        list1.sort()
    
    for i in lenoflist:
        if i != word1:
            for j in i:
                list_word.append(j)
            list_word.sort()
            if list_word == list1:
                anagrams.append(i)
                lenoflist.remove(i)
                list_word = []
            else:
                list_word = [] 
    return anagrams

for k in lenoflist:
    anagramfinal.append(anagramfinder(k))

anagramfinal1 = []

for l in anagramfinal:
    if len(l) >= 2:
        anagramfinal1.append(l)
anagramfinal1.sort()    

listres = []

for m in anagramfinal1:
    listres.append(m)
for n in listres:
    f1.write("\n" + str(n))

f1.close()
f.close()    





    
            

            
        

        
