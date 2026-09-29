class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        chain = []

        for asteroid in asteroids:
            destroyed = False

            while chain and asteroid < 0 and chain[-1] > 0:
                last_el = chain[-1]

                if abs(asteroid) == abs(last_el):
                    chain.pop()
                    destroyed = True
                    break

                if abs(asteroid) > abs(last_el):
                    chain.pop()
                    # Asteroid survived, so check the next item in chain.
                    continue

                if abs(asteroid) < abs(last_el):
                    destroyed = True
                    break

            if not destroyed:
                chain.append(asteroid)

        return chain