class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [(target - pos)/sp for (pos, sp) in sorted(zip(position, speed), reverse=True)]
        fleets, curr = 0, -1
        for time in times:
            if curr < time:
                curr = time
                fleets += 1
        return fleets
        
# Approach: Since road is single lane and overtaking is not possible, we have to start from the car with
# highest position (say X) even if there are faster car beyond that. This is because each car has to either
# join the X's fleet or make separate fleet. If any car's time to target is less than the X's time, those will
# meet before reaching target and hence will be part of same fleet. If any car's time to target is more than
# current time (X's time), then this car will have separate fleet. This will be repeated for all cars to get
# total number of fleets.
# See this for visual representation: https://www.youtube.com/watch?v=H5w6doOXz10