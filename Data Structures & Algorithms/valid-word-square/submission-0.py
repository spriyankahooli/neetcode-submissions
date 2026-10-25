class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        cols = 0 
        rows = len(words)

        for row in range(rows):
            for col in range(len(words[row])):
                if col >= rows or row >= len(words[col]) or words[row][col] != words[col][row]:
                    return False
        return True
    