def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)-1):
            if nums[i] + nums[i+1] == target:
                output = [i, i+1]
        return output