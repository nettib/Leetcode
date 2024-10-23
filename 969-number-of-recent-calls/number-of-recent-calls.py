class RecentCounter:
    def __init__(self):
        self.request=[]
    def ping(self, t: int) -> int:
        count = 0
        requests = 0
        if self.request == []:
            self.request.append(t)
            requests+=1
        else:
            for time in self.request:
                if t - 3000 <= time < t:
                    requests+=1
                else:
                    count+=1
            del self.request[:count]
            self.request.append(t)
            requests += 1
        return requests

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)