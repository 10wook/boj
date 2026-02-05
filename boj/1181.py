N = int(input())
L = []
for i in range(N):
    L.append(input())
S = set(L)

L = list(S)
# print(L)
answer = []
for i in L:
    if len(answer) != 0:
        add = 0
        for j in range (len(answer)):
            # print(answer[j])
            if len(i) == len(answer[j]):
                if i < answer[j]:
                    answer.insert(j,i)
                    add = 1
                    break
            elif len(i) < len(answer[j]):
                answer.insert(j,i)
                add = 1
                break
            else:
                pass
        if add == 0 and j ==(len(answer) -1):
            answer.append(i)
            
    else:
        answer.append(i)
for i in answer:
    print(i)