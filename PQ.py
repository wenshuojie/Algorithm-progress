# 优先级队列

class MaxPQ: # 最大堆（每个节点都比它的两个子节点大）

    def __init__(self) -> None:
        self.pq = [None] # [0]不放元素
        self.size = 0

    def max(self):
        return self.pq[1]

    def insert(self, e):
        self.size += 1
        # 放在最后，再上浮
        self.pq.append(e)
        self.swim(self.size)

    def delMax(self):
        max = self.pq[1]
        self.pq[1], self.pq[self.size] = self.pq[self.size], self.pq[1]
        self.pq[self.size] = None
        self.size -= 1
        self.sink(1)
        return max
    
    # 上浮第x个元素
    def swim(self, x):
        # 堆顶无法继续上浮
        while x > 1 and self.pq[self.parentInd(x)] < self.pq[x]:
            self.pq[self.parentInd(x)], self.pq[x] = self.pq[x], self.pq[self.parentInd(x)]
            x = self.parentInd(x)

    # 下沉第x个元素 
    # TODO:自己可以改一下
    def sink(self, x):
        while self.leftInd(x) <= self.size:
            older = self.leftInd(x)
            if self.rightInd(x) <= self.size and self.pq[older] < self.pq[self.rightInd(x)]:
                older = self.rightInd(x)
            if self.pq[older] < self.pq[x]:
                break
            self.pq[older], self.pq[x] = self.pq[x], self.pq[older]
            x = older


    def parentInd(self, nodeInd):
        return nodeInd // 2

    def leftInd(self, nodeInd):
        return nodeInd * 2
    
    def rightInd(self, nodeInd):
        return nodeInd * 2 + 1
    

