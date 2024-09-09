class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        # The filnal result will be put here
        out = [[1]]

        for i in range(1, numRows):
            prev = out[i-1]
            new = [1]
            for j in range(1, i):
                new.append(prev[j-1] + prev[j])
            new.append(1)
            out.append(new)

        return out
        