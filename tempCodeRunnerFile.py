N = int(input())
L = []
for i in range(N):
    L.append(i)
S = set(L)

L = list(S)

answer = []
for i in L:
    if len(answer) != 0:
        add = 0
        for j in range (len(answer)):
            print(answer[j])
            if len(i) == len(answer[j]):
                if i < answer[j]:
                    pass
                if i > answer[j]:
                    answer.insert(j,i)
                    add =1
            elif len(i) < len(answer[j]):
                answer.insert(j,i)
                add =1
            else:
                pass
        if add == 0 and j ==(len(answer) -1):
            answer.append(i)
            
    else:
        answer.append(i)