class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        sum_cnt = [0] * 100
        for c in word:
            num = ord(c) - 65
            sum_cnt[num] += 1
        
        is_special = [0] * 26
        cur_cnt = [0] * 100
        for c in word:
            num = ord(c)-65
            cur_cnt[num]+=1
            if c>= 'A' and c<='Z' and is_special[num]==0 and cur_cnt[num+32] == sum_cnt[num+32] and cur_cnt[num]==1 and sum_cnt[num+32]!=0:
                is_special[num] = 1
        
        sum = 0
        for c in is_special:
            sum += c 
        
        return sum