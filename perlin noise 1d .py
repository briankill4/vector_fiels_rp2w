import math

class PerlinNoise:
    def __init__(self, seed=0):
        self.perm = list(range(256))
        for i in range(256):
            self.perm[i] = (self.perm[i] + seed) & 255
        self.perm += self.perm

    def fade(self, t):
        return t * t * t * (t * (t * 6 - 15) + 10)

    def lerp(self, a, b, t):
        return a + t * (b - a)

    def grad(self, hash, x):
        h = hash & 15
        grad = 1 + (h & 7)
        if h & 8:
            grad = -grad
        return grad * x

    def noise(self, x):
        xi = int(x) & 255
        xf = x - int(x)
        u = self.fade(xf)

        a = self.perm[xi]
        b = self.perm[xi + 1]

        return (self.lerp(self.grad(a, xf), self.grad(b, xf - 1), u) + 1) / 2

