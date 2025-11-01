class FrequencyTracker(object):

    def __init__(self):
        self.arr = []
        self.hashArr = {}
        self.hashfreq = {}

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        self.arr.append(number)
        if number in self.hashArr:
            self.hashfreq[self.hashArr[number]] -= 1
            if self.hashfreq[self.hashArr[number]] == 0:
                del self.hashfreq[self.hashArr[number]]
        self.hashArr[number] = self.hashArr.get(number, 0) + 1
        self.hashfreq[self.hashArr[number]] = self.hashfreq.get(self.hashArr[number], 0) + 1

    def deleteOne(self, number):
        """
        :type number: int
        :rtype: None
        """
        if number in self.hashArr:
            temp = self.hashArr[number]
            self.hashfreq[temp] -= 1
            self.hashArr[number] -= 1
            if self.hashArr[number] == 0:
                del self.hashArr[number]
            if self.hashfreq[temp] == 0:
                del self.hashfreq[temp]
            if number in self.hashArr:
                self.hashfreq[self.hashArr[number]] = self.hashfreq.get(self.hashArr[number], 0) + 1

    def hasFrequency(self, frequency):
        """
        :type frequency: int
        :rtype: bool
        """
        if frequency in self.hashfreq:
            return True
        return False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)