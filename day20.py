from load_data import load_data


class Range:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def _parse_range(d):
    sep = d.index('-')
    return(int(d[:sep]), int(d[sep+1:]))


def _parse_intvls(data):
    idx = 0
    L = len(data)
    while idx < L-1:
        if data[idx+1].b > data[idx].b and data[idx+1].a - 1 <= data[idx].b:
            data[idx].b = data[idx+1].b
            del data[idx+1]
            L = len(data)
        elif data[idx+1].a < data[idx].b and data[idx+1].b < data[idx].b:
            del data[idx+1]
            L = len(data)
        else:
            idx += 1
    return data


def getRangeList(data):
    data = sorted([_parse_range(d) for d in data])
    datarange = [Range(*d) for d in data]
    datarange = _parse_intvls(datarange)
    return datarange


def _count_allowed(data):
    ctr = data[0].a - 0
    for j in range(len(data) - 1):
        ctr += data[j+1].a - data[j].b - 1
    ctr += 2**32 - 1 - data[-1].b
    return ctr

if __name__ == "__main__":
    data = load_data('./input/day20.txt')
    data = getRangeList(data)

    print('Part 1')
    print('\tFirst IP is: {}.'.format(data[0].b + 1))
    # Answer: 32259706

    print('\nPart 2')
    ctr = _count_allowed(datarange)
    print('\tNumber allowed IPs: {}.'.format(ctr))
    # Answer: 113
