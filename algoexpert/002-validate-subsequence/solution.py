# Time Complexity O(n) | Space Complexity O(1)

def isValidSubsequence(array, sequence):
    # Write your code here.
    index = 0
    for i in range(len(array)):
        if array[i] == sequence[index]:
            index += 1
        if len(sequence) == index:
            return True
    return False

