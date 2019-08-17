import copy
n, m, q = list(map(int, input().split()))

G = {}
for i in range(1, n + 1):
    G[i] = {}

for i in range(m):
    a, b, c = list(map(int, input().split()))
    G[a][b] = c

def getEdges(G):
    v1 = []
    v2 = []
    w = []
    for i in G:
        for j in G[i]:
            if G[i][j] != 0:
                w.append(G[i][j])
                v1.append(i)
                v2.append(j)
    return v1, v2, w


def Bellman_Ford(G, v0, INF=999):
    v1, v2, w = getEdges(G)
    dis = dict((k, INF) for k in G.keys())
    dis[v0] = 0

    # 核心算法
    for k in range(len(G) - 1):
        check = 0
        for i in range(len(w)):
            if dis[v1[i]] + w[i] < dis[v2[i]]:
                dis[v2[i]] = dis[v1[i]] + w[i]
                check = 1
        if check == 0:
            break
    return dis

for i in range(q):
    M=copy.deepcopy(G)
    s, l, r, p = list(map(int, input().split()))
    for j in range(l, r + 1):
        if j in M[s].keys():
            M[s][j] = min(G[s][j], p)
        else:
            M[s][j] = p
    dis = Bellman_Ford(M, 1)
    print(dis[n])

'''
3 5 3
1 2 7
2 3 6
1 3 9
2 1 2
3 1 1
1 2 3 8
2 3 3 1
2 1 3 5
'''