N = int(input())
L=[]
for i in range(N):
    L.append(int(input()))
    
zerocall = [1,0]
onecall = [0,1]    
for i in range(max(L)-1):
    zerocall.append(-1)
    onecall.append(-1)

def check_zerocalls(num:int):

        if zerocall[num] != -1:
            return zerocall[num]
        else : 
            zerocall[num] = (check_zerocalls(num-2)+check_zerocalls(num-1))
            return zerocall[num]



def check_onecalls(num:int):
    
        if onecall[num] != -1:
            return onecall[num]
        else : 
            onecall[num] = (check_onecalls(num-2)+check_onecalls(num-1))
            return onecall[num]
        
for i in L:
    print(check_zerocalls(i),check_onecalls(i))
