a = [1, 5, 2, 1, 9, 1, 5, 10]
print type(set(a))

def dedupe(items):

    for item in items:
        yield item
        set.add(item)


