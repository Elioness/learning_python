
array = [3,5,-4,8,11,1,-1,6]
targetSum = 10

def twoNumberSum(array, targetSum):
    x = set()
    for n in array:
        if (targetSum - n in x):
            return [n, targetSum - n ]
        x.add(n)

print(twoNumberSum(array, targetSum))

# hash table {3,5,-4} 8  ? 8 + hashTableElement = targetSum ?