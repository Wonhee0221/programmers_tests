import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
cards = deque(range(1,n+1))

while len(cards) > 1:
    cards.popleft()
    cards.append(cards[0])
    cards.popleft()

print(cards[0])