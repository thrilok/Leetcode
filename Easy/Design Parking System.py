class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.big>0:
            self.big -=1
            return True
        elif carType == 2 and self.medium>0:
            self.medium -=1
            return True
        elif carType == 3 and self.small>0:
            self.small -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)


# Runtime: 128 ms, faster than 97.09% of Python3 online submissions for Design Parking System.
# Memory Usage: 14.7 MB, less than 74.11% of Python3 online submissions for Design Parking System.
