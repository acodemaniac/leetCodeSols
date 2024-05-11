class Solution(object):
    def imageSmoother(self, img):
        m = len(img)
        n=len(img[0])
        res=[[0 for z in range(n)] for h in range(m)]
        for i in range(m):
            for j in range(n):
                adj = []
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < len(img) and 0 <= nj < len(img[0]):
                            adj.append(img[ni][nj])
                res[i][j]=(sum(adj)/len(adj))
        return res