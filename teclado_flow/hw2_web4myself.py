def check_arr_odd(arr):
    return arr.index('odd') in arr

print(check_arr_odd(['even', 4, 'odd', 55, 'even', 2]))

def find_sum(n):
    return sum([i for i in range(n+1) if i%3==0 or i%5==0])

print(find_sum(5))
print(find_sum(10))


names = ['ryan', 'mark', 'max', 'johny']
def get_names(names):
    return [i for i in names if len(i)==4]

print(get_names(names))