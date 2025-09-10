def palind(r):
    s=0
    e= len(r) -1
    while(s<e): 
       if (r[s]!=r[e]):
            return False
       s+=1
       e-=1
    
    return True
r=("n","o","p","n")
if(palind(r)):
        print("the tuple is flip-flop")
else:
        print("the tuple is not flip-flop")
