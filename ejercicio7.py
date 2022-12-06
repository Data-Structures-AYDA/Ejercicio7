import random
import sys
import json

# total arguments
n = sys.argv

# sort and store the sorted list in hashmap, O(nlogn) time, O(n) space


class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sortedNums = sorted(nums, reverse=True)
        numsMap = {}
        for i in range(len(sortedNums)):
            if i == 0:
                numsMap[sortedNums[i]] = 'Gold Medal'
            elif i == 1:
                numsMap[sortedNums[i]] = 'Silver Medal'
            elif i == 2:
                numsMap[sortedNums[i]] = 'Bronze Medal'
            else:
                numsMap[sortedNums[i]] = str(i+1)
        result = []
        for num in nums:
            result.append(numsMap[num])
        return result


# create 100 test cases


def createTestCases(cant: int = 100):
    testCases = []
    for i in range(cant):
        testCases.append(random.sample(range(100), 5))
    return testCases


# with open(n[1], 'w') as f:
#     testCases = createTestCases()
#     for i in range(len(testCases)):
#         f.write(str(testCases[i]) + '\n')

with open(n[1], 'r') as f:
    testCases = f.readlines()
    for i in range(len(testCases)):
        print(Solution().findRelativeRanks(json.loads(testCases[i].strip())))
                