num = int (input())
count=0
for i in range(num):
    word = str(input())
    GW = 1 #1이면 그룹 단어라는 뜻
    if len(word) == 1:
        count+=1
        continue
    
    for l in range (len(word)-1 ): #숫자 횟수만큼 반복하면서 진행할거니까.
        
        if word[l] in word[l+1:] :
            if word[l+1]== word[l]:
                pass
            else :
                GW =0
                break
        else : 
            pass

    
    if GW == 1 :
        count+=1

print(count)