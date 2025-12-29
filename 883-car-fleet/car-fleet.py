class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        for i in range(len(position)):
            position[i] = (position[i], speed[i])
        
        position.sort()
        position = position[::-1]
        
        fleet = []

        for i in range(len(position)):
            time = (target - position[i][0]) / position[i][1]
            if fleet and fleet[-1] >= time:
                pass
            else:
                fleet.append(time)
        
        return len(fleet)