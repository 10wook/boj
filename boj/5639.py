import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

preorder = []
while True:
    line = input().rstrip()
    if not line:
        break
    preorder.append(int(line))

def post_order(start, end):
    if start >= end:
        return
    root = preorder[start]
    mid = start + 1
    while mid < end and preorder[mid] < root:
        mid += 1
    post_order(start + 1, mid)
    post_order(mid, end)
    print(root)

post_order(0, len(preorder))
