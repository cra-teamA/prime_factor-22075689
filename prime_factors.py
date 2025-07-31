class PrimeFactor:
    def of(self, number) -> []:
        print("Let's Find out Prime Factor!")
        factors = []
        divisor = 2
        while number > 1:
            while number % divisor == 0:
                factors.append(divisor)
                number //= divisor
            divisor += 1
        return factors
