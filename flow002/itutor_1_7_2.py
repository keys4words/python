n=int(input())
journal={}
for i in range(n):
    temp_el=[i for i in input().split(' ')]
    if temp_el[0] in journal:
        journal[temp_el[0]].append(int(temp_el[1]))
    else:
        journal[temp_el[0]]=[int(temp_el[1])]

for k in journal.keys():
    if len(journal[k])>1:
        journal[k]=sum(journal[k])/len(journal[k])
    else:
        journal[k]=float(journal[k][0])

for k in sorted(journal):
    print(k, round(journal[k],1))

