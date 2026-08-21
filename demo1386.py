class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reservedSeats.sort(key = lambda x: (x[0] , x[1]))
        sum = 0

        row = 1
        idx = 0
        
        limits = [1] * 10

        while row <= n and idx < len(reservedSeats):
            if reservedSeats[idx][0] > row:
                sum += self.could_seats(limits)
                self.clean(limits)
                row += 1
            else: # 当前判断行 等于 限制的idx
                limits[reservedSeats[idx][1]-1] = 0
                idx+=1
        
        if idx == len(reservedSeats):
            sum += self.could_seats(limits)
        
        sum += max((n-row),0) * 2
        
        return sum

    def could_seats(self,limits):
        cnt = 0
        if limits[1]==1 and limits[2]==1 and limits[3]==1 and limits[4]==1:
            cnt +=1
        
        if limits[5] == 1 and limits[6]==1 and limits[7]==1 and limits[8]==1:
            cnt +=1
        
        if cnt == 0:
            if limits[4]==1 and limits[5] == 1 and limits[6]==1 and limits[3]==1:
                cnt+=1
        
        return cnt
            
    def clean(self,limits):
        for i in range(10):
            limits[i]=1

            