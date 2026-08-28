import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nw_num = [-1 * nums[i] for i in range(len(nums))]
        heapq.heapify(nw_num)
        count = 0
        while count < k - 1:
            heapq.heappop(nw_num)
            count += 1
        return -1 * nw_num[0]