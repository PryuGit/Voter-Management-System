c1=0
c2=0
c3=0
dict={}
n=int(input("Enter Number of Voters:"))
while (n<=0):
    print("Invalid Voter Count!!")
    n=int(input("Enter Number of Voters:"))
for x in range(n):
    c=input("Choose candidate(C1/C2/C3):").upper()
    if(c=="C1"):
        c1=c1+1
        dict.update({"C1":c1})
    elif(c=="C2"):
        c2=c2+1
        dict.update({"C2":c2})
    elif(c=="C3"):
        c3=c3+1
        dict.update({"C3":c3})
    else:
        print("Invalid Data")

value={k:v for k,v in sorted(dict.items(), key=lambda item:item[1])}
reverse={k:v for k,v in sorted(dict.items(), key=lambda item:item[1],reverse="true")}
print(value)
print(reverse)

