def alg(N):
    b = bin(N)[3:]
    i = int(b,2)
    return (N-i)

a = []
for x in range (10, 1001):
    y = alg(x)
    if y not in a:
        a.append(y) 
print (len(a))