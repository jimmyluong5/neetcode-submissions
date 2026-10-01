class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        window = set()

        for right in range(len(nums)):
            if right - left > k:
                #resize the window
                window.remove(nums[left])
                left+=1
            if nums[right] in window:
                return True
            #add it to the window
            window.add(nums[right])
        return False
        