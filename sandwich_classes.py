class Pool:
    def __init__(self, _R0, _R1, _fee):
        self.R0 = _R0
        self.R1 = _R1
        self.K = self.R0 * self.R1
        self.fee = _fee

    def swap(self, amount_in, token_in, min_price):
        if token_in:
            amount_out = (self.R0 - self.R0 * self.R1 / (self.R1 + amount_in)) * self.fee
            self.R0 -= amount_out
            self.R1 += amount_in
            assert self.R0 / self.R1 > min_price
        else:
            amount_out = (self.R1 - self.R1 * self.R0 / (self.R0 + amount_in)) * self.fee
            self.R1 -= amount_out
            self.R0 += amount_in
            assert self.R1 / self.R0 > min_price
        return amount_out

    def resetPool(self, _R0, _R1):
        self.R0 = _R0
        self.R1 = _R1
        self.K = self.R0 * self.R1

