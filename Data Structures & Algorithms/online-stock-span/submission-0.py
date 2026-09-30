class StockSpanner:

    def __init__(self):
        self.ledger = []

    def next(self, price: int) -> int:

        ledger = self.ledger
        
        ledger.append(price)

        ptr = -1
        count = 0
        while ptr >= -len(ledger):
            
            if ledger[ptr] > price:
                break

            count += 1
            ptr -= 1
            
        return count