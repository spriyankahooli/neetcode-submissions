class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l,r =0, len(nums)-1
        while l<r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l =m+1
            else:
                r =m
        pivot = l
        left, right =0,len(nums)-1
        if nums[pivot]<=target<=nums[right]:
            left =pivot 
        else:
            right=pivot-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]== target:
                return mid 
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return -1
        