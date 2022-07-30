
# Time complexity O(n^2) | Space Complexity O(1)
def twoNumberSum(array, targetSum):
    # Write your code here.
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
    return []


# Time complexity O(nlog(n)) | Space Complexity O(2)

def twoNumberSum(array, targetSum):
    # Write your code here.
    array = sorted(array)
    start = 0
    end = len(array) - 1

    while start < end:
        if array[start] + array[end] == targetSum:
            return [array[start] , array[end]]
        elif array[start] + array[end] < targetSum:
            start += 1
        else:
            end -= 1
    return []


# Time complexity O(n) | Space Complexity O(k)
def twoNumberSum(array, targetSum):
    # Write your code here.
    hash_map = {}
    for item in array:
        if (targetSum - item) in hash_map:
            return [hash_map[targetSum - item], item]
        hash_map[item] = item
    return []

