
t=input("Enter the string: ")
vowel=0
cons=0
counter=0
for i in range(0,len(t)):
    if(t[i]!=" "):
        if(t[i]=="a" or t[i]=="e" or t[i]=="i" or t[i]=="o" or t[i]=="u" or
        t[i]=="A" or t[i]=="E" or t[i]=="I" or t[i]=="O" or t[i]=="U"):
            vowel=vowel+1
        else:
            cons=cons+1
    else:
        counter= counter+1
print("Total Vowels=", vowel)
print("Total Consonents=", cons)
print("Totle number of space=",counter)
