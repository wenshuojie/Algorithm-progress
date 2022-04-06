a = [8,2,6,3,1]
diff = []
diff.append(a[0])
for i in range(1,len(a)):
    diff.append(a[i]-a[i-1])

res = []
res.append(diff[0])
for i in range(1,len(diff)):
    res.append(diff[i] + res[i-1])

print(res)