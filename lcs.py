

def lcs(s1: str, s2: str) -> str:
    m = len(s1)
    n = len(s2)
    suff = [ [0 for x in range(m + 1)] for y in range(n + 1)]

    x = '_' + s1
    y = '_' + s2
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[j] == y[i]:
                suff[i][j] = suff[i - 1][j - 1] + 1
            else:
                suff[i][j] = max(suff[i - 1][j], suff[i][j - 1])

    return suff[n][m]

if __name__ == '__main__':
    s1 = 'abcbdab'
    s2 = 'bdcaba'
    print(lcs(s1, s2))
