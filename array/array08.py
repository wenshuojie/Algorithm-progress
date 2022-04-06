# 1094. 拼车
class Difference:
    def __init__(self) -> None:
        self.diff = [0]*10001

    def update(self,startindex,endindex,inc):
        self.diff[startindex] += inc
        if (endindex+1 < len(self.diff)):
            self.diff[endindex+1] -= inc
    
    def result(self):
        res = [0]*len(self.diff)
        res[0] = self.diff[0]
        for i in range(1,len(self.diff)):
            res[i] = res[i-1] + self.diff[i]
        return res

# trip[i] = [numPassengersi, fromi, toi]
def carPooling(trips, capacity):
    car = Difference()
    for trip in trips:
        # 车上区间是[fromi,toi-1]，因为toi已经下车了
        car.update(startindex=trip[1],endindex=trip[2]-1,inc=trip[0])

    results = car.result()

    for result in results:
        if result > capacity:
            return False
    return True

if __name__ == '__main__':
    result = carPooling([[2,1,5],[3,5,7]],3)
    print(result)