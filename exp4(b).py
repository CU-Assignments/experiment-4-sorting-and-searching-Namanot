import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        L_element = []
        for i in nums:
            heapq.heappush(L_element, i)
            if len(L_element) > k:
                heapq.heappop(L_element)
        return L_element[0]