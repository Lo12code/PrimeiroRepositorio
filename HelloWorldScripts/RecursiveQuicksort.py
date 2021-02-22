list = [1,32,40,43,21,54,10,1,16,1,40,76,34]

def quicksort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        lowers = [i for i in list[1:] if i <= pivot]
        highers = [j for j in list[1:] if j > pivot]
        return quicksort(lowers) + [pivot] + quicksort(highers)



def uniquequicksort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        lowers = [i for i in list[1:] if i < pivot]
        highers = [j for j in list[1:] if j > pivot]
        return uniquequicksort(lowers) + [pivot] + uniquequicksort(highers)
