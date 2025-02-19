class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        length = len(nums)
        if length <= 1 or length <= k:
            return nums

        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        bucket = [None] * (length + 1)
        for num, freq in freq.items():
            if bucket[freq] is None:
                bucket[freq] = [num]
            else:
                bucket[freq].append(num)       
        kMost = []

        for numList in reversed(bucket):
            if numList is None:
                continue

            kMost = kMost + numList

            if len(kMost) == k:
                return kMost