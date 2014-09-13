class Solution:

    # @param s, a string

    # @param dict, a set of string

    # @return a boolean

    def wordBreak(self, s, dict):

        if len(s)<=0 or len(dict)<=0: return False

        def wordB(s,i,dict):

            there = 0

            if len(s) == 0: return 0

            if s[:i] in dict: there += 1

            if s[i:] in dict: there += 1
            return there+wordB(s[:i],0,dict)+wordB(s[i+1:],0,dict)

            

        if wordB(s,0,dict) >0: return True

        else: return False

print Solution().wordBreak("a",["a"])

