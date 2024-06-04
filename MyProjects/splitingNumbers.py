def splitHighestValue(nums):
    if len(nums)<2:
        return nums

    highest = max(nums)
    numCopy = nums[:]
    numCopy.remove(highest)
    nextHighest = max(numCopy)

    remainingPart = highest - nextHighest

    indexofHighest = nums.index(highest)
    result = nums[:indexofHighest] + [nextHighest, remainingPart] + nums[indexofHighest+1:]

    return result

nums = [4,8,6,3,2]
result = splitHighestValue(nums)
print(result)