class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        top = set("QWERTYUIOPqwertyuiop")
        mid = set("ASDFGHJKLasdfghjkl")
        bot = set("ZXCVBNMzxcvbnm")
        
        return [word for word in words if set(word).issubset(top) or set(word).issubset(mid) or set(word).issubset(bot)]
        
