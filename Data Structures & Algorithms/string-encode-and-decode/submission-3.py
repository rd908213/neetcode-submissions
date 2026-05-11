class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for i in strs:
            output = output + str(len(i)) + '#' + i
        return output

    def decode(self, s: str) -> List[str]:
        solution = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            string = s[j+1:j+1+length]
            solution.append(string)
            i = j + 1 + length

        return solution