from re import M


nums = [10,30,40,45,70,80,85,90,100]
words = ["at", "ball", "cat", "dog", "eye", "fish", "good"]
unsorted = [30, 20, 70, 40, 50, 100, 90]
# // Search an array for an item using the binary search algorithm.
# // If item found, return index where found, else return -1.
def binarySearch(listName, element) :
    upperIndex = len(listName) - 1
    lowerIndex = 0
    while lowerIndex <= upperIndex:
        middleIndex = (upperIndex+lowerIndex) // 2
        if listName[middleIndex] == element:
            return middleIndex
        elif element < listName[middleIndex]:
            upperIndex = middleIndex - 1
        else:
            lowerIndex = middleIndex + 1
    return -1

print(binarySearch(nums, 100))
print(binarySearch(nums, 75))
print(binarySearch(words, "fish"))
print(binarySearch(words, "at"))
print(binarySearch(unsorted, 70))