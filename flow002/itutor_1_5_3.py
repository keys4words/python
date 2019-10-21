s=input()
first=s.find('h')
last=s.rfind('h')
start=s[:first+1]
end=s[last:]
middle=s[first+1:last]
res=start+middle[::-1]+end
print(res)