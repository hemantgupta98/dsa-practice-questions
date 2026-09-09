class Solution:
    def findMajority(self, arr):
        n = len(arr)
        count = {}
        ans = []

        for num in arr:
            count[num] = count.get(num, 0) + 1

        for num in count:
            if count[num] > n // 3:
                ans.append(num)

        ans.sort()
        return ans

obj = Solution()

arr = [5, 3, 2, 3, 2, 2, 1, 3]

print(obj.findMajority(arr))    