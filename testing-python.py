nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog","at", "good", "eye", "cat", "ball", "fish"]

def bubbleSort(anArray):
    n = len(anArray)
    for i in range(n):
        for j in range(n - 1):
            if anArray[j] > anArray[j+1]:
                anArray[j], anArray[j+1] = anArray[j+1], anArray[j]

 
bubbleSort(nums)
bubbleSort(words)
print(nums)
print(words)
