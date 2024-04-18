class ListUtil:
    # sort list of list
    @classmethod
    def sortListOfLists(cls, lst):
        lst.sort()
        for it in lst:
            it.sort()
