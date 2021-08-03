from queue import PriorityQueue

q = PriorityQueue()
[n,m] = list(map(int,input().split()))
a = list(map(int,input().split()))
d = {}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i] = 1
    q.put((-d[i],-i))
    print(-q.queue[0][1],-q.queue[0][0])
