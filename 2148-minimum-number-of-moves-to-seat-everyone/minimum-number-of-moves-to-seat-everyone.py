class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        res = 0

        for st, se in zip(students, seats):
            res += abs(st - se)

        return res