gondora,group = list(map(int,input().split()))

jyousya = [int(input()) for i in range(gondora)]
ninzuu = [int(input()) for l in range(group)]

print(jyousya)
print(ninzuu)
i=0
res = 0
#goukei = sum(ninzuu)
#while goukei == 0:
  
if jyousya[i] < ninzuu[i]:
    nokori = ninzuu[i] - jyousya[i]

print(nokori)
#i += 1