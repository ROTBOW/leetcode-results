from heapq import heappush, heappop

# heappush(heap, val) - adds val to our heap
# heappop(heap) - gives us the min val in the heap

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # create heap
        # loop over stones
        #    add - ver of the stone to our heap
        # 
        # loop as long as heap has more than 1
        #   get the top of our heap, ABS the stone, save to stone1
        #   pop the next stone off the stone, ABS it, save to stone2
        #   if stone1 is equal to stone2
        #       go back to heap
        #   else get the diff of the stones
        #       send the diff into the heap
        #
        # return what is left in the heap as long as it has something in it and ABS it
        # else return 0

        heap = list()

        for stone in stones:
            heappush(heap, -(stone))

        while len(heap) > 1:
            stone1 = abs(heappop(heap))
            stone2 = abs(heappop(heap))

            if stone1 == stone2:
                continue
            else:
                heappush(heap, -(stone1 - stone2))

        return abs(heap[-1]) if heap else 0