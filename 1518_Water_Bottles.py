class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        bottles = [1] * numBottles
        total_drink = 0
        empty_bottles = 0

        i = 0
        while i < len(bottles):
            total_drink += 1
            empty_bottles += 1

            if empty_bottles == numExchange:
                bottles.append(1)
                empty_bottles = 0
            i += 1
        return total_drink 