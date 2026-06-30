class Solution:
    def calculateHours(self, piles, eatingRate):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / eatingRate)

        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return math.ceil(piles[0] / h)

        maxPile = max(piles)
        # Find leftmost boundary of maxPile using binary search that satisfies eating all piles within time limit
        bottom, top = 0, maxPile

        while bottom < top:
            mid = bottom + (top - bottom) // 2
            hoursNeeded = self.calculateHours(piles, mid)
            # calculated hours less than the limit, we try to decrease the rate, 
            # including the current rate in possible answers
            if hoursNeeded <= h:
                top = mid
            # calculated hours more than the limit, we increase the limit, 
            # excluding current rate from possible answers
            else:
                bottom = mid + 1
        
        # when search is completed bottom points to leftmost boundary of possible rates
        return bottom