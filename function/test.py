class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(results, result, candidates, target, level):
            if target == 0:
                results.append(list(result))
                return
            elif target > 0:
                for i in range(level, len(candidates)):
                    result.append(candidates[i])
                    dfs(results, result, candidates, target - candidates[i], i)
                    result.pop()

        results = []
        dfs(results, [], candidates, target, 0)
        return results

a = Solution()
b = a.combinationSum([2,3,5],8)
print(b)
def aa():
    print("yes")