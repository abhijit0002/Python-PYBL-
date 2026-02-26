class Solution:
    def median(self, mat):
        arr = [num for row in mat for num in row]
    
        n = len(arr)
        
        arr.sort()
        
        if n % 2 == 1:
            return arr[n // 2]
        
        else:
            middle1 = arr[n // 2 - 1]
            middle2 = arr[n // 2]
            return (middle1 + middle2) / 2

