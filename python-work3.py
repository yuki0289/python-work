def my_find(l, x):
    if x in l:
        return (l.index(x))+1
    else:return -1

n,k = list(map(int,input().split()))


list1 = [int(input()) for i in range(n)]
res = my_find(list1,k)

print(res)