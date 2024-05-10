class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for a in asteroids:
            if a <= mass:
                mass += a
            else:
                return False

        return True

# beats 52.19% runtime and 15.92% memory
# https://leetcode.com/problems/destroying-asteroids/submissions/1223239182/
