N,M = map(int,input().split())
answer = float('inf')
inputs = [input() for _ in range(N)]
board1 = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
board2 = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW','WBWBWBWB']

for i in range(0,N-8+1):
    for j in range(M-8+1):
        cnt1 = 0
        cnt2 = 0
        for ii in range(8):
            for ij in range(8):
                if inputs[i+ii][j+ij] != board1[ii][ij]:
                    cnt1+=1
                if inputs[i+ii][j+ij] != board2[ii][ij]:
                    cnt2+=1
        answer = min (answer,cnt1,cnt2)
print(answer)