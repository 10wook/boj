num = int (input())
count=0
for i in range(num):
    word = list(str(input()))

    # print(word)
    word_set = set(word)
    
    for l in word_set:
        word_temp = word[:]
        print(word_temp)
        bb= True
        for j in range(word_temp.count(l)-1):
            
            # if word_temp.count(l)==1:
            #     pass
            last = word_temp.index(l)
            print(last)
            word_temp.pop(word_temp.index(l))
            print(word_temp.index(l))
            if last != word_temp.index(l):
                bb = False#얘가 false 면 그룹 단어가 아님
                break
            if last == word_temp.index(l):
                pass
    if bb== False :
        pass
        # break
    else: 
        count = count + 1

print(count)