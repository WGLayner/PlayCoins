import hiker
import unittest

class TestHiker(unittest.TestCase):

    def test_life_the_universe_and_everything(self):
        '''simple example to start you off'''
        douglas = hiker.Hiker()
        self.assertEqual(42, douglas.answer())

    def test_two_sequence_num(self):
        '''test two sequence num'''
        douglas = hiker.Hiker()
        iList = [10, 5, 1]
        iDime = 20
        lExpectedList = []
        lExpectedList1 = [[0,0,20], [0, 1, 15], [0,2,10], [0,3,5], [0,4,0]]
        lExpectedList2 = [[1,0,10], [1, 1,5],[1,2,0]]
        lExpectedList3 = [[2,0,0]]
        lExpectedList = lExpectedList1 + lExpectedList2 + lExpectedList3
        lRealList = douglas.get_solution(iDime, iList)
        self.assertEqual(lExpectedList,lRealList)
        iDime = 15
        lExpectedList = []
        lExpectedList1 = [[0, 0, 15], [0, 1, 10], [0, 2, 5], [0, 3, 0]]
        lExpectedList2 = [[1, 0, 5], [1, 1,0]]
        lExpectedList = lExpectedList1 + lExpectedList2
        lRealList = douglas.get_solution(iDime, iList)
        self.assertEqual(lExpectedList, lRealList)
        iDime = 100
        iList = [25, 10, 5, 1]
        lRealList = douglas.get_solution(iDime, iList)
        iLen = len(lRealList)
        print('iLen = ', iLen)
        self.assertEqual(True, iLen>20)



    def test_get_two_value_list(self):
        '''test get_two_value_list function'''
        douglas = hiker.Hiker()
        lTwoValue = douglas.get_two_value_list(20,[5,1])
        lExpectedList = [[0,20], [1, 15], [2,10],[3,5],[4,0]]
        self.assertEqual(lExpectedList, lTwoValue)
        lTwoValue = douglas.get_two_value_list(0, [5,1])
        lExpectedList = [[0,0]]
        self.assertEqual(lExpectedList, lTwoValue)

    def test_form_new_list(self):
        '''test form new list function'''
        douglas = hiker.Hiker()
        iList = [[5,1], [0,10]]
        iA = 2
        newList = [[2,5,1],[2,0,10]]
        self.assertEqual(newList, douglas.form_new_list(iA, iList))

    def test_compare_two_list(self):
        '''test if two list are same'''
        douglas = hiker.Hiker()
        iList1 = [ 3, 8, 9, 5, 1]
        iList2 = [ 3, 8, 9, 5, 1]
        self.assertEqual(True, douglas.compare_two_list(iList1, iList2))


if __name__ == '__main__':
    unittest.main()
