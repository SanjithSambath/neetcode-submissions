class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def operand(first, second, operand):

            if operand == "+":
                return int(first) + int(second)
            if operand == "-":
                return int(first) - int(second)
            if operand == "*":
                return int(first) * int(second)
            if operand == "/":
                return int(first / second)

        ledger = []

        for item in tokens:
                    
            if item in ["+", "-", "*", "/"]:
                answer = operand(ledger[-2], ledger[-1], item)
                ledger.pop(-1)
                ledger.pop(-1)
                ledger.append(answer)

            else: 
                ledger.append(int(item))

        return ledger[0]