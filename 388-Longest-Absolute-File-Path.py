class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        if not input: return 0
        
        maxLen = 0
        pathDir = {}
        pathList = input.split('\n')
        
        for elt in pathList:
            name = elt.strip('\t')
            fileDepth = len(elt)-len(name)
            # check for file
            if '.' in elt:
                maxLen = max(maxLen, pathDir.get(fileDepth-1,0)+len(name))
            else: # add the length to this dir plus length of this dir plus one for '\'
                pathDir[fileDepth] = pathDir.get(fileDepth-1,0)+len(name)+1
        
        return maxLen
