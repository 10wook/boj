import sys
input = sys.stdin.readline
nums = int(input())
for i in range(nums):
    a,b = map(int,input().split())
    I=i+1
    answer = a+b
    print(f'Case #{I}: {a} + {b} = {answer}')