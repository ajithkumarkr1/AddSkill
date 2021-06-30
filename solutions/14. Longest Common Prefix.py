class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """        
        prefix = ""
        # longest possible prefix is checked first and returned if satisfiable
        for x in reversed(range(len(min(strs, key=len)))):
            prefix += strs[0][0:x+1]
            # compare prefix of first string to all other strings
            for y in range(1,len(strs)):
                # prefixes don't match, move to next prefix
                if (prefix != strs[y][0:x+1]):
                    prefix = ""
                    break
            # suitable prefix found
            if (prefix != ""):
                return prefix
        # no suitable prefix, return ""
        return prefix
