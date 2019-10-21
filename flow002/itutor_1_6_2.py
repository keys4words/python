n=[int(i) for i in input().split(' ')]
n_even=[n[j] for j in range(0,len(n),2)]
print(sum(n_even)*n[-1])