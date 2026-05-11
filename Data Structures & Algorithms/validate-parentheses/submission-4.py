class Solution:
    def isValid(self, s: str) -> bool:
        brackMap = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        point = 0
        brackList = [] # List of unaccounted for brackets (openings)
        while point < len(s):
            if s[point] in brackMap.keys():
                brackList.append(s[point])
            elif s[point] in brackMap.values():
                print(brackList)
                if len(brackList) == 0 or s[point] != brackMap[brackList[-1]]:
                    return False
                else:
                    brackList.pop()
            point += 1
        
        if len(brackList) == 0:
            return True
        else:
            return False