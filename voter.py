class Voter:
    def __init__(self,n=0):
        self.n=n
        
    def voter_count(self):#COUNTING VOTERS
        print("======================================")
        print("Voting System")
        print("======================================")
        
        while True:
            try:
                n=int(input("Enter Number of Voters:"))
                if n>0:
                    self.n=n
                    return n
                else: 
                    print("Invalid, Enter Number:")
            except ValueError:
                print("Invalid, Enter Number:")
        return self.n
 
class Vote(Voter):  
    def __init__(self,c1=0,c2=0,c3=0,vote_dict=None):
        self.c1=c1
        self.c2=c2
        self.c3=c3
        self.dict={} if vote_dict is None else vote_dict
        
    def  vote(self,n):#VOTING CANDIDATES
        r=Result(None,None)
        print("======================================")
        print("Candidates")
        print("( $ ) for Navin")
        print("( & ) for Nick")
        print("( * ) for Borat")
        print("--------------------------------------")
        for x in range(n):
            while True:
                c=input("Choose candidate:")
                if c == "$":
                    self.c1 += 1
                    self.dict["Navin"] = self.c1
                    break
                elif c == "&":
                    self.c2 += 1
                    self.dict["Nick"] = self.c2
                    break
                elif c == "*":
                    self.c3 += 1
                    self.dict["Borat"] = self.c3
                    break
                else:
                    print("Invalid Data! Choose $, &, or *.")
        r.value={k:v for k,v in sorted(self.dict.items(), key=lambda item:item[1])}
        r.reverse={k:v for k,v in sorted(self.dict.items(), key=lambda item:item[1],reverse="true")}
        return r.value,r.reverse      
         
class Result(Vote):
    
    def __init__(self,value=None,reverse=None):
        self.value=value
        self.reverse=reverse
        
    def result(self,value,reverse):#DISPLAY RESULT
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
    

def main():
    
    cast=Voter()
    count=cast.voter_count()
    
    system=Vote()
    ascending,descending=system.vote(count)
    
    display=Result()
    display.result(ascending,descending)
    
if __name__=="__main__":
    main()



