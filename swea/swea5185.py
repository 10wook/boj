import sys
input  = sys.stdin.readline
T = int(input())
digitals ={'0':'0000',
           '1':'0001',
           '2':'0010',
           '3':'0011',
           '4':'0100',
           '5':'0101',
           '6':'0110',
           '7':'0111',
           '8':'1000',
           '9':'1001',
           'A':'1010',
           'B':'1011',
           'C':'1100',
           'D':'1101',
           'E':'1110',
           'F':'1111',}
           
for test_num in range(1,T+1):
    answer = ''
    a,b =input().split()
    for i in b:
        answer = answer + digitals[i]
    print(f'#{test_num} {answer}')