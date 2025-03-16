try:
    from multiprocessing import cpu_count, Process
    from os import system, chdir
except:
    print()

cpu = 45


def fib(n):
    return fib(n - 1) + fib(n - 2) if n > 1 else 1

def worker():
    return fib(cpu)


if __name__ == '__main__':
    cpus = cpu_count()
    for _ in range(cpus):
        Process(target=worker).start()