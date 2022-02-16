list = [1,2,3,4,8,9,4,]
# // Search an array for an item using the linear search algorithm.
# // If item found, return index where found, else return -1.
def linearSearch() :
    n = -1
    for i in list:
        n += 1
        if i == 9:
            return n
    return -1
print(linearSearch())