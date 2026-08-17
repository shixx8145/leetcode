class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        arr = [0]*100
        for c in word:
            arr[ord(c)-65] = 1
        
        cnt = 0
        for idx in range(32):
            if arr[idx]!=0 and arr[idx+32]!=0:
                cnt+=1
        
        return cnt