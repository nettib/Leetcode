class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        while j < len(typed):
            if j == 0:
                if typed[j] != name[i]:
                    return False
            else:
                if i != len(name):
                    if typed[j] != name[i]:
                        if typed[j] != typed[j-1]:
                            return False
                else:
                    if typed[j] != name[i - 1]:
                        if typed[j] != typed[j-1]:
                            return False
            if i != len(name):
                if typed[j] == name[i]:
                    i+=1
            j+=1
        if i == len(name):
            return True
        return False
        # i = 0
        # j = 0
        # while j < len(typed):
        #     if typed[j] not in name:
        #         return False
        #     if i == len(name):
        #         if typed[j] != name[i-1]:
        #             return False
        #     elif name[i] is typed[j]:
        #         i+=1
        #     elif name[i] != typed[j] and typed[j] != typed[j-1]:
        #         return False
        #     j+=1
        # if i == len(name):
        #     return True
        # return False