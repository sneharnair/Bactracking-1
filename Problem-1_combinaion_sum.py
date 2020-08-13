# APPROACH 1: Recursive 
# Time Complexity : O(n * 2 ^ n), n: len(candidates)
# Space Complexity : O(n * 2 ^ n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None
#
#
# Your code here along with comments explaining your approach
# 1. At each index, two options, maintain current sum and current path locally (each time pass a copy of the path)
# 2. If choose -> update current sum and path (can choose the same lement again) , If don't choose -> inc. index. Recursively call the function
# 3. If the current sum is equal to target, add current path to the global var result.

class Solution:
    def __init__(self):
        self.result = []
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        if not candidates:
            return None
        
        self.helper(candidates, target, 0, 0, [])
        return self.result
    
    def helper(self, candidates, target, curr_sum, index, curr_path):
        # base case
        if index >= len(candidates) or curr_sum > target:
            return
        if curr_sum == target:
            self.result.append(curr_path)
            return
        
        # logic case        
        # don't choose
        self.helper(candidates, target, curr_sum, index + 1, copy.deepcopy(curr_path))
        
        # choose     
        curr_path.append(candidates[index])
        self.helper(candidates, target, curr_sum + candidates[index], index, copy.deepcopy(curr_path))
        
        
        
# APPROACH  BACKTRACK
# Time Complexity : O(n * 2 ^ n), n: len(candidates)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None 
#
#
# Your code here along with comments explaining your approach
# 1. Explore all paths for each ind of candidates
# 2. 1st action -> append current element to path, 2nd -> recurse on the same index, as same element can be chosen again (from which pivot again and explore all paths), 
#     3rd -> backtrack (undo the action, remove the element from the list.
# 3. If the current sum is equal to target, add current path to the global var result.

class Solution:
    def __init__(self):
        self.result = []
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if candidates is None:
            return None
        
        self.helper(candidates, target, 0, [], 0)
        return self.result
    
    
    def helper(self, candidates, target, curr_sum, curr_path, index):
        # base 
        if index >= len(candidates) or curr_sum > target:
            return
        if curr_sum == target:
            self.result.append(copy.deepcopy(curr_path))
            return
        
        # logic
        for pos in range(index, len(candidates)):
            # action
            curr_path.append(candidates[pos])
            
            # recurse
            self.helper(candidates, target, curr_sum + candidates[pos], curr_path, pos)
            
            # backtrack
            curr_path.pop()
       
