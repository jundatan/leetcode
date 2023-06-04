class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 0:
            return []
        strs_dict = {}
        for x in strs:
            sorted_str = sorted(list(x))
            sorted_str = ''.join(sorted_str)
            if sorted_str in strs_dict:
                strs_dict[sorted_str].append(x)
            else:
                strs_dict[sorted_str] = []
                strs_dict[sorted_str].append(x)
        return strs_dict.values()
