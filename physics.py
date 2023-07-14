class Physics:
    def __init__(self) -> None:
        self.gravity = 9.8

    def calc_speed(self, d, t):
        self.speed = d / t
        return self.speed

    def calc_PE(self, m, h):
        result = m * self.gravity * h
        return result

    def calc_force(self, m, a):
        result = m * a
        return result

    def velocity(self, u, a, t):
        result = u + (a * t)
        return result

    def pressure(self, f, a):
        result = f / a
        return result