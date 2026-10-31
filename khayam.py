n =8
khayam=[]
for i in range(n+1):
    row=[1]*(i+1)
    for j in range(1,i):
        row[j] = khayam[i-1][j-1] +khayam[i-1][j]
    khayam.append(row)
print ("8:")
for row in khayam:
    print(row)
