class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dic = defaultdict(list)
        result = []

        for i in range(len(nums)):
            dic[nums[i]].append(nums[i])
        
        sorted_list = sorted(dic.values(), key=len, reverse=True)

        for i in sorted_list[:k]:
            result.append(i[0])
        
        return result