T = int(input())

def subsequence_check(Long:list,short:list):
    if short[0] not in Long:
        return False
    else:#들어있다면?? 들어있다면 거기까지 짤라야지
        if len(short) == 1:
            return True
        else:
            return subsequence_check(Long[Long.index(short[0])+1:],short[1:])


for i in range(1,T+1):
    _ = input()
    Long = list(map(int,input().split()))
    short = list(map(int,input().split()))
    if subsequence_check(Long,short):
        answer = 'YES'
    else:
        answer = "NO"


    print(f'#{i} {answer}')