class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for x in strs:
            count=[0]*26
            for c in x:
                count[ord(c) - ord('a')] += 1
            key = tuple(count) 
            if key not in output:
                output[key] = [x]
            else:
                output[key].append(x)  
        return list(output.values())  