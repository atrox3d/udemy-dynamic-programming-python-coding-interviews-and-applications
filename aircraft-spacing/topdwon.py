def max_passengers(i, passengers, cache:dict={}):
    if i >= len(passengers):
        return 0

    if (best := cache.get(i, None)) is not None:
        return best

    first = passengers[i] + max_passengers(i + 2, passengers, cache)
    no_first = max_passengers(i+1, passengers, cache)
    best = max(first, no_first)

    cache[i] = best
    return best


def get_planes(num_planes, max_passengers):
    import random
    return [random.randint(1, max_passengers) for _ in range(num_planes)]


planes = [155, 44, 1, 96, 67, 203, 3]
planes = get_planes(20, 200)
print(planes)

print(max_passengers(0, planes))
