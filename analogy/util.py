import itertools


def while_yield(f):
    x = f()
    while x:
        yield x
        x = f()


def chunk(chunksize, vals):
    it = iter(vals)

    def next():
        return list(itertools.islice(it, chunksize))

    yield from while_yield(next)

