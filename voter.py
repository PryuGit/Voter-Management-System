def  vote(n):#VOTING CANDIDATES
    c1=0
    c2=0
    c3=0
    dict={}
    print("======================================")
    print("Candidates")
    print("( $ ) for Navin")
    print("( & ) for Nick")
    print("( * ) for Borat")
    print("--------------------------------------")
    for x in range(n):
        c=input("Choose candidate:").upper()
        if(c=="$"):
            c1=c1+1
            dict.update({"Navin":c1})
        elif(c=="&"):
            c2=c2+1
            dict.update({"Nick":c2})
        elif(c=="*"):
            c3=c3+1
            dict.update({"Borat":c3})
        else:
            print("Invalid Data")
    value={k:v for k,v in sorted(dict.items(), key=lambda item:item[1])}
    reverse={k:v for k,v in sorted(dict.items(), key=lambda item:item[1],reverse="true")}
    return value,reverse

def result(value,reverse):#DISPLAY RESULT
    print("--------------------------------------")
    ans=input("Descending or Ascending??(D/A):")
    if ans.upper() == 'A':
        print("Ascending\n",value)
    elif ans.upper() == 'D':
        print("Descending\n",reverse)
    else:
        while ans.upper()!='A' and ans.upper()!='D':
            print("Error in the system.")
            ans=input("Descending or Ascending??(D/A):")
        if ans.upper() == 'A':
            print("Ascending\n",value)
        elif ans.upper() == 'D':
            print("Descending\n",reverse)
    print("======================================")         
    
def voter_count():#COUNTING VOTERS
    print("======================================")
    print("Voting System")
    print("======================================")
    n=int(input("Enter Number of Voters:"))
    while (n<=0):
        print("Invalid Voter Count!!")
        n=int(input("Enter Number of Voters:"))
    return n

count=voter_count()
ascending,descending=vote(count)
result(ascending,descending)





