class Solution:
    def calPoints(self, operations: List[str]) -> int:

        ledger = []
        running_sum = 0
        
        for operation in operations:

            if operation not in ["+", "D", "C"]:
                ledger.append(int(operation))
                running_sum += int(operation)

            if operation == "+":
                if len(ledger) >= 2: 
                    last = ledger[-1]
                    second_to_last = ledger[-2]
                    ledger.append(last + second_to_last)
                    running_sum += (last + second_to_last)

                if len(ledger) == 1: 
                    running_sum += (ledger[-1])
                    ledger.append(ledger[-1])
            
            if operation == "D":
                if len(ledger) >= 1: 
                    running_sum += (2 * ledger[-1])
                    ledger.append(2 * ledger[-1])
            
            if operation == "C":
                if len(ledger) >= 1: 
                    running_sum -= (ledger[-1])
                    ledger.pop()
    
        return running_sum
                