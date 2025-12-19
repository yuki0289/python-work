n,m = list(map(int,input().split()))

pay = list(map(int,input().split()))

point = [i//100 for i in pay]
point_all = sum(point)
req = (m-point_all)*100
res = max(0,req)
print(res)
