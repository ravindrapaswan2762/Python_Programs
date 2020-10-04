import time
from functools import lru_cache

@lru_cache(maxsize=2)  # latest three work ko hi cach karega
def some_work(n):
    # some task taking n second
    time.sleep(n)
    return n

if __name__ ==  '__main__':
    print("now running some work")

    some_work(3)
    some_work(9)
    some_work(4)
    some_work(2)
    print("done....calling again")


    some_work(3)
    print("called again")