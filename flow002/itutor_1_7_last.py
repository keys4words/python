import operator

n=int(input())
text=[]
freg={}
for i in range(n):
    line=input().lower()
    line=line.replace(':', ' ')
    line=line.replace(';', ' ')
    line=line.replace("'", ' ')
    line=line.replace('!', ' ')
    line=line.replace('?', ' ')
    line=line.replace('.', ' ')
    line=line.replace(',', ' ')
    line=line.strip().split(' ')
    for word in line:
       text.append(word)

for word in text:
    freg[word]=text.count(word)

sorted_text=sorted(freg.items(), key=operator.itemgetter(1))
print(*sorted_text[-1])