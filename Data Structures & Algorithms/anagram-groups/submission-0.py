class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        saved = defaultdict(list)
        for s in strs:
            k = ''.join(sorted(s)) 
            saved[k].append(s)
        return list(saved.values())