from collections import deque

x, y = 1, 1

with open("data.txt", "r") as f:
    for line in f:
        row_data = line.strip().split('|') 
        miro.append(row_data)

print(miro)



while 1:
    if miro[x][y] == 'T':
        print(miro[x][y])
        break
    elif miro[x][y + 1] == '#':
        y += 1
        miro[x][y] = '-'

    elif miro[x][y + 1] == 'T':
        y += 1
        miro[x][y] = '-'
        break

    elif miro[x+1][y] == "":
        x += 1
        miro[x][y] = '-'

    elif miro[x + 1][y] == '#':
        x += 1
        miro[x][y] = '-'
        break
for row in miro:
    print(''.join(row))

# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))

f.close()

