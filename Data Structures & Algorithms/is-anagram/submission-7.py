class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList = []
        for c in s:
            sList.append(c)
        sList.sort()

        tList = []
        for c in t:
            tList.append(c)
        tList.sort()

        return sList == tList