#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import heapq
import sys

n = int(input())
lst = []
for _ in range(n):
    heapq.heappush(lst, int(sys.stdin.readline()))

if len(lst) == 1:
    print(0)
else:
    answer = 0
    while len(lst) > 1 :
        temp1 = heapq.heappop(lst)
        temp2 = heapq.heappop(lst)
        answer += temp1 + temp2
        heapq.heappush(lst,temp1 + temp2)
        
    print(answer)

