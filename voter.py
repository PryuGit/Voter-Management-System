class Voter:
    def __init__(self,n=0):
        self.n=n
        
    def get_voter(self):   
        return self._n
    
    def set_voter(self,n):
        self._n=n
        
    def voter_count(self):#COUNTING VOTERS
        print("======================================")
        print("Voting System")
        print("======================================")
        
        while True:
            try:
                n=int(input("Enter Number of Voters:"))
                if n>0:
                    self.set_voter(n)
                    return self.get_voter()

                else: 
                    print("Invalid, Enter Number:")
            except ValueError:
                print("Invalid, Enter Number:")
 
class Vote(Voter):  
    def __init__(self,c1=0,c2=0,c3=0,vote_dict=None):
        self._c1=c1
        self._c2=c2
        self._c3=c3
        self._dict={} if vote_dict is None else vote_dict
        
    def  vote(self,n):#VOTING CANDIDATES
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
                    self._c1 += 1
                    self._dict["Navin"] = self._c1
                    break
                elif c == "&":
                    self._c2 += 1
                    self._dict["Nick"] = self._c2
                    break
                elif c == "*":
                    self._c3 += 1
                    self._dict["Borat"] = self._c3
                    break
                else:
                    print("Invalid Data! Choose $, &, or *.")
        return self.sorted_data()
    def sorted_data(self):   
        value={k:v for k,v in sorted(self._dict.items(), key=lambda item:item[1])}
        reverse={k:v for k,v in sorted(self._dict.items(), key=lambda item:item[1],reverse="true")}
        return value,reverse      
         
class Result():
    
    def __init__(self,value=None,reverse=None):
        self._value=value
        self._reverse=reverse
    
    def get_ascending(self):
        return self._value 
    
    def get_descending(self):
        return self._reverse
    
    def result(self,value,reverse):#DISPLAY RESULT
        self._value=value
        self._reverse=reverse
        
        print("--------------------------------------")
        ans=input("Descending or Ascending??(D/A):")
        if ans.upper() == 'A':
            print("Ascending\n",self.get_ascending())
        elif ans.upper() == 'D':
            print("Descending\n",self.get_descending())
        else:
            while ans.upper()!='A' and ans.upper()!='D':
                print("Error in the system.")
                ans=input("Descending or Ascending??(D/A):")
            if ans.upper() == 'A':
                print("Ascending\n",self.get_ascending)
            elif ans.upper() == 'D':
                print("Descending\n",self.get_descending)
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



