class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        length = len(s)
        f = [0] * length # couldarrive ? 
        sum = [0] * (length+1) # 前几个数的和,
        sum[1] = 1
        for idx in range(1,length):
            if s[idx] == '0':
                f[idx] = (sum[max(0 , idx - minJump+1)] - sum[max(0,idx-maxJump)] )> 0
            
            sum[idx+1] = sum[idx] + f[idx]

        
        return f[-1] == 1