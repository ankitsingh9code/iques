'''
Given an integer array nums, return all the triplets [nums[i]],[nums[j]],[nums[k]] 
such that i!=j, i!=k, j!=k and nums[i] + nums[j] + nums[k] == 0 
Notice that the soution set must not contain duplicate triplet
'''

class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        
        result = []
        for i in range(0,len(nums)):
            # print(f"===={i}====")
            for j in range(0,len(nums)-1-i):
                # print(j)
                if 0-(nums[i]+nums[j]) in nums :
                    k_index = nums.index(0-(nums[i]+nums[j]))
                    if i!=j and i!=k_index and j!=k_index and nums[i] + nums[j] + nums[k_index] == 0 :
                        # print(i,j,k_index)
                        mylist= [nums[i],nums[j],nums[k_index]]
                        mylist.sort()
                        # print(mylist)
                
                        if mylist not in result:
                            result.append(mylist)

        print(result)
        return result
solution = Solution()
# solution.threeSum([-1,0,1,2,-1,-4, 6,3,2,1])
solution.threeSum([1,-1,0,1,2,-1,-4])

