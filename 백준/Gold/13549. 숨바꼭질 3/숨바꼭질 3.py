from collections import deque
MAX = 100001


def bfs():
    Q = deque()
    Q.append((n, 0))
    visited = [False]*MAX
    visited[n] = True

    while True:
        now, time = Q.pop()
        if now == k:
            return time

        nxt = 2*now
        if 0 < nxt < MAX and not visited[nxt]:
            visited[nxt] = True
            Q.append((nxt, time))

        nxt = now-1
        if 0 <= nxt < MAX and not visited[nxt]:
            visited[nxt] = True
            Q.appendleft((nxt, time+1))

        nxt = now+1
        if 0 <= nxt < MAX and not visited[nxt]:
            visited[nxt] = True
            Q.appendleft((nxt, time+1))


n, k = map(int, input().split())
print(bfs())
