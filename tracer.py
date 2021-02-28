#Tracer.py
#By Deon Fourie
# 10 May

print("***** Program Trace Utility *****")
fname = input("Enter the name of the program file: ")
f = open(fname, "r")
lines = f.readlines()

f1 = open(fname, "w")
indiceslist = []
newindiceslist = []
noflist = []
newlist = []
resultlist = []

def insert(liness):
    lines.insert(0, '"""DEBUG"""')
    for i in lines:
        if i[:3] == "def":
            indiceslist.append(lines.index(i))
            noflist.append("'" + i[4:i.index("(")] + "'")      
    
    for j in range(len(indiceslist)):
        newlist.append(j)
    for k in indiceslist:
        k = k + newlist[indiceslist.index(k)]
        newindiceslist.append(k)
    
    for l in newindiceslist:
            lines.insert(l+1, '''    """DEBUG""";print(''' + noflist[newindiceslist.index(l)] + ''')''')
    
    for y in lines:
        if y[len(y)-1:] == "\n":
            y = y.replace("\n", "")        
            resultlist.append(y)
        else:
            resultlist.append(y)

def remove(liness):
    lines.remove(lines[0])
    for i in lines:
        if i[4:15] == '"""DEBUG"""':
            lines.remove(i)
            
    for j in lines:
        if j[len(j)-1:] == "\n":
            j = j.replace("\n", "")
            resultlist.append(j)
        else:
            resultlist.append(j)

if lines[0] != '"""DEBUG"""\n':
    result = str(insert(lines))
    f1.close()
    f2 = open(fname, "a")
    for i in resultlist:
        f2.write("\n" + str(i))
    f2.close()
    print("Inserting...Done") 
        
else:
    result = str(remove(lines))
    f1.close()
    f2 = open(fname, "a")
    for i in resultlist:
        f2.write("\n" + str(i))
    f2.close()
    print("Removing...Done")
      
f.close()






    

    


