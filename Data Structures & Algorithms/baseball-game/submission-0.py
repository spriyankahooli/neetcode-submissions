class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []

        for op in (operations):
            if op == "D":
                result.append(result[-1] * 2)
            elif op == "+":
                result.append(result[-2] + result[-1])
            elif op == "C":
                result.pop()
            else:
                result.append(int(op))

        return sum(result)
        