import time

def powers(limit):
    return [x**2 for x in range(limit)]


def measure_runtime(func):
    start = time.time()
    func()
    end = time.time()
    print(end-start)


measure_runtime(lambda : powers(500000))

