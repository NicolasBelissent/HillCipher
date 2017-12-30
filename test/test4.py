import numpy as np


def cut(l):
    segments = []
    z = l % 3
    q = int(np.floor(l / 3))
    if z == 0:
        for i in range(0, q):
            segments.append(3)
    elif z == 1:
        for i in range(0, q):
            segments.append(3)
        segments.append(2)
        segments.append(2)
    elif z == 2:
        for i in range(0, q):
            segments.append(3)
        segments.append(2)

    return segments


def split(l):
    list = []
    segmentLengths = cut(len(l))
    offset = 0
    for k in segmentLengths:
        segment = []
        for i in range(0, k):
            segment.append(l[offset])
            offset = offset + 1
        list.append(segment)

    return list


h = split("hello")
print(h)
