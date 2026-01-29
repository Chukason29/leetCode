"""
1️⃣ Two Sum

Given an array of integers called "nums" and an integer "target", return the indices of the two numbers such that they add up to target.

📌 Each input has exactly one solution
📌 You may not use the same element twice
"""

nums = [2, 9, 7, 4, 3]
target =  12


def twoSums(nums, target):
    twoSumsList = []
    for i in range(len(nums)):
        for k in range(len(nums)):
            if i == k:
                continue
            if (nums[i]+ nums[k]) == target:
                twoSumsList.append(i)
                twoSumsList.append(k)
                return twoSumsList

    
#More Proffesional Solution

def myTwoSums(nums, target):
    for i in range(len(nums)):
        for k in range(i + 1, len(nums)):
            if (nums[i] + nums[k]) == 12:
                return [i, k]

print (myTwoSums(nums, target))