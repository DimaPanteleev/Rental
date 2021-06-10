from generalList import GeneralList


class GeneralListEdit(GeneralList):
    def getNewID(self):
        m = 0
        for c in self.getIDs():
            if c > m:
                m = c
        return m + 1
