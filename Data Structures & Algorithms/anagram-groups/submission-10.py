class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = defaultdict(list)

        for s in strs:
            str_map["".join(sorted(s))].append(s)
        
        return [v for v in str_map.values()]
