

def f():
    n, m = map(int, input().split())

    a =[]
    
    for i in range(n):
        a.append(input().split())
        
    k = 0
    
    for i in range(n):
        for j in range(m):
            try:
                if a[i][j] == 'A' and a[i][j+1] == '.':
                    a[i][j+1] = 'A'
                else:
                    print(k)
                    return
            except:
                pass
        k += 1

f()


