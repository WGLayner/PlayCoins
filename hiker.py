class Hiker:

    def answer(self):
        return 6 * 7

    def get_solution(self, iTarget, iList):
        k = iList[0]
        m = iTarget/k
        n = int(m) + 1
        solution_list = []
        if len(iList) > 2:
            for i in range(0, n):
                iNextTarget = iTarget - i*k
                new_list = self.get_solution(iNextTarget, iList[1:])
                new_list = self.form_new_list(i, new_list)
                solution_list = solution_list + new_list
            return solution_list
        else:
            new_list = self.get_two_value_list(iTarget, iList)
            return new_list



    def get_two_value_list(self, iTarget, iList):
        lTwoValueList = []
        k = iList[0]
        m = iTarget/k
        n = int(m) + 1
        for i in range(0, n):
            iValue = iTarget - i*k
            new_list = [i, iValue]
            lTwoValueList.append(new_list)
        return lTwoValueList


    def form_new_list(self, iA, iList):
        for k in iList:
            k.insert(0, iA)
        return iList

    def compare_two_list(self, iList1, iList2):
        iLen1 = len(iList1)
        iLen2 = len(iList2)
        if ( iLen1 != iLen2):
            return False
        for i in range(iLen1):
            if (iList1[i] != iList2[i]):
                return False
        return True
        
