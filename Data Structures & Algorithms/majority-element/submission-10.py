class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_count = Counter(nums)
        sorted_num_count = sorted(
            num_count.items(),
            key=lambda item: item[1],
            reverse=True
        )
        
        target = len(nums) // 2
        for e, v in sorted_num_count:
            if v > target:
                return e
