class Fibonacci:

    def calculate(self, n: int) -> int:
        if n < 0:
            raise ValueError("n must be greater than or equal to 0")
        if n == 0 or n == 1:
            return n
        return self.calculate(n - 1) + self.calculate(n - 2)