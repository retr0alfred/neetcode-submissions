class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        result = []
        for index, val in enumerate(strs):
            temp = ''.join(sorted(val))
            if temp not in d:
                d[temp] = (index,)
            else:
                d[temp] += (index,)
        x = d.values()
        for i in x:
            templst = []
            for j in i:
                templst.append(strs[j])
            result.append(templst)
        return result