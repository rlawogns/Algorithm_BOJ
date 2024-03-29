from sys import stdin
dic={(0,0,0):1}
def w(a,b,c):
    if (a,b,c) in dic:
        return dic[(a,b,c)]
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if a < b and b < c:
        dic[(a,b,c)]=w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dic[(a,b,c)]
    else:
        dic[(a, b, c)] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return dic[(a,b,c)]
a,b,c=map(int,stdin.readline().split())

while not(a==-1 and b==-1 and c==-1):
    print("w({0}, {1}, {2}) = {3}".format(a,b,c,w(a,b,c)))
    a, b, c = map(int, stdin.readline().split())