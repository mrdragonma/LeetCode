from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 寻找旋转递增数组中的最小值
        # 题解153
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1

if __name__ == '__main__':
    # 题解153
    nums = [4,5,1,2,3]
    print(Solution().findMin(nums))


