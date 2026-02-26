class Solution:
    def findMinDiff(self, arr, M):
        
        n = len(arr)
       
        if M == 0 or n == 0 or M > n:
            return 0
        arr.sort()
        min_diff = float('inf')
        for i in range(n - M + 1):
            current_diff = arr[i + M - 1] - arr[i]
            if current_diff < min_diff:
                min_diff = current_diff

        return min_diff
