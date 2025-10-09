import sys
input = sys.stdin.readline
connects = [[1, 3], [0, 2], [1, 5], [0, 6], [], [2, 8], [3, 7], [6, 8], [5, 7]]

for _ in range(int(input())):
    board = sum([list(input().rstrip()) for _ in range(3)], [])
    group = []
    visited = [False] * 9
    for start in range(9):
        if board[start] == 'O' and not visited[start]:
            count = 1
            visited[start] = True

            st = [start]
            while st:
                now = st.pop()
                for connect in connects[now]:
                    if board[connect] == 'O' and not visited[connect]:
                        visited[connect] = True
                        count += 1
                        st.append(connect)
            group.append(count)

    _, *numbers = map(int, input().split())
    print(1 if sorted(group) == numbers else 0)