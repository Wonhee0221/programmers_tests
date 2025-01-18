import sys
input = sys.stdin.readline

num_list = list(map(int,input().split()))
num_list.sort()
print(num_list[-2])