class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        if digits[0] == 0:
            return [1] + digits

        return digits

        # two cases
        # looking for theses cases while loop backwards
        # digits[i] == 9 OR not be 9

        # case 1, it is 9
        # change 9 to 0, and let our loop continue

        # case 2, it is NOT 9
        # up the number by one at that index, and return digits

        # if digits is only 9s, ie like [9, 9]
        # so after its gone through it would look like this [0, 0]
        # so if our first number, after looping is zero, we know that we need to add a 1
        # we can return [1] + digits ([0, 0]) => [1, 0, 0]