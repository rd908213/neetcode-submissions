class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        strsSort = [''.join(sorted(s)) for s in strs]
        for i in range(len(strsSort)):
            if strsSort[i] not in map:
                map[strsSort[i]] = [i]
            else:
                map[strsSort[i]].append(i)

        answer = []
        for j in map.values(): # j = [1, 3, 7]
            answer.append([strs[k] for k in j])
        return answer