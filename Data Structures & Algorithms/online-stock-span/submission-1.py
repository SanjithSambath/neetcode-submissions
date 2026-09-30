class StockSpanner:

    def __init__(self):
        self.ledger = []

    def next(self, price: int) -> int:
        span = 1  # Today

        while self.ledger and self.ledger[-1][0] <= price:
            old_price, old_span = self.ledger.pop()
            span += old_span

        self.ledger.append((price, span))
        return span