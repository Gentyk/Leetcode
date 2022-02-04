# Remote duplicates from a sorted array without creating a new array

def removeDuplicates(nums: list) -> int:
    if len(nums) < 2:
        return len(nums)
    i = 0
    while True:
        if i == len(nums) - 1:
            break
        if nums[i] == nums[i+1]:
            del nums[i+1]
        else:
            i+=1
    return len(nums)


