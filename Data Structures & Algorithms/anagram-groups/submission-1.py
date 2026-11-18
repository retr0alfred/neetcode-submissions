class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d1 = {}
        for index, val in enumerate(strs):
            temp = ''.join(sorted(val))
            if temp not in d1:
                d1[temp] = (index,)
            else:
                d1[temp] += (index,)
        result = []
        for i in d1.values():
            temp = []
            for j in i:
                temp.append(strs[j])
            result.append(temp)
        return result