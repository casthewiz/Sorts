def partition(sortMe, start, finish):
    pivot = sortMe[finish]
    i = start
    for j in range(start, finish + 1):
        if sortMe[j] < pivot:
            tmp = sortMe[i]
            sortMe[i] = sortMe[j]
            sortMe[j] = tmp
            i += 1
    tmp = sortMe[i]
    sortMe[i] = sortMe[finish]
    sortMe[finish] = tmp
    return i

def qsort(sortMe, start, finish):
    if start < finish:
        newPart = partition(sortMe, start, finish)
        qsort(sortMe, start, newPart-1)
        qsort(sortMe, newPart+1, finish)
    else:
        return None
