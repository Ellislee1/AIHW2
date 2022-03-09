import unittest

import numpy as np

from TilePlacementProblem import main

class TestCases(unittest.TestCase):
    def testZerosSuccess(self):
        # Test that the system is successful when the space is all zeros and full blocks with no goals
        l = np.zeros((16,4,4))
        C = {
            "OUTER_BOUNDARY": 0,
            "FULL_BLOCK": 16,
            "EL_SHAPE": 0
            }
        T = [0,0,0,0]

        result = main(l,C,T)
        self.assertTrue(result)
    
    def testZerosFail(self):
        # Test that the system fails when the target is all zeros
        l = np.zeros((100,4,4))
        C = {
            "OUTER_BOUNDARY": 50,
            "FULL_BLOCK": 0,
            "EL_SHAPE": 50
            }
        T = [0,0,0,0]

        result = main(l,C,T)
        self.assertFalse(result)

    def testZerosFailTarget(self):
        # Test that the system fails when there is a target in an all zero env
        l = np.zeros((100,4,4))
        C = {
            "OUTER_BOUNDARY": 50,
            "FULL_BLOCK": 0,
            "EL_SHAPE": 50
            }
        T = [0,1,15,26]

        result = main(l,C,T)
        self.assertFalse(result)
    
    def testSimpleSuccess(self):
        # Test that the system fails when there is a target in an all zero env
        l = np.ones((1,4,4))
        C = {
            "OUTER_BOUNDARY": 1,
            "FULL_BLOCK": 0,
            "EL_SHAPE": 0
            }
        T = [4,0,0,0]

        result = main(l,C,T)
        self.assertTrue(result)
    
    def testSimpleFail(self):
        # Test that the system fails when there is a target in an all zero env
        l = np.ones((1,4,4))
        C = {
            "OUTER_BOUNDARY": 1,
            "FULL_BLOCK": 0,
            "EL_SHAPE": 0
            }
        T = [8,0,0,0]

        result = main(l,C,T)
        self.assertFalse(result)
    
    def test44Ones(self):
        l = np.ones((4,4,4))
        C = {
            "OUTER_BOUNDARY": 1,
            "FULL_BLOCK": 2,
            "EL_SHAPE": 1
            }
        T = [13,0,0,0]

        result = main(l,C,T)
        self.assertTrue(result)

    def testMediumOnes(self):
        np.random.seed(114)
        l = np.random.randint(0,2,(4,4,4))
        C = {
            "OUTER_BOUNDARY": 1,
            "FULL_BLOCK": 1,
            "EL_SHAPE": 2
            }
        T = [12,0,0,0]

        result = main(l,C,T)
        self.assertTrue(result)

    def testMediumOnesTwos(self):
        np.random.seed(119)
        l = np.random.randint(0,3,(4,4,4))
        C = {
            "OUTER_BOUNDARY": 1,
            "FULL_BLOCK": 1,
            "EL_SHAPE": 2
            }
        T = [8,4,0,0]

        result = main(l,C,T)
        self.assertTrue(result)

    def testMediumOnesTwosThrees(self):
        np.random.seed(119)
        l = np.random.randint(0,4,(4,4,4))
        C = {
            "OUTER_BOUNDARY": 2,
            "FULL_BLOCK": 1,
            "EL_SHAPE": 1
            }
        T = [2,3,7,0]

        result = main(l,C,T)
        self.assertTrue(result)

    def testMediumOnesTwosThreesFours(self):
        np.random.seed(119)
        l = np.random.randint(0,5,(9,4,4))
        C = {
            "OUTER_BOUNDARY": 5,
            "FULL_BLOCK": 1,
            "EL_SHAPE": 3
            }
        T = [10,7,10,10]

        result = main(l,C,T)
        self.assertTrue(result)

    def testSampleExample(self):
        l = np.array([[[2,2,1,3]
,[0,2,1,3]
,[2,1,0,0]
,[0,3,2,0]]
,[[4,2,3,4]
,[2,4,1,0]
,[4,3,1,4]
,[2,1,1,1]]
,[[1,0,0,3]
,[0,1,3,1]
,[0,3,0,2]
,[1,3,1,1]]
,[[2,1,0,1]
,[4,2,0,0]
,[3,1,4,3]
,[3,2,2,4]]
,[[0,2,2,1]
,[0,1,4,3]
,[3,2,1,2]
,[4,0,3,4]]
,[[0,3,4,0]
,[2,2,0,0]
,[0,2,2,4]
,[1,0,1,1]]
,[[4,4,0,2]
,[1,1,1,4]
,[3,3,1,4]
,[4,4,3,4]]
,[[0,3,2,2]
,[3,2,3,2]
,[3,4,3,3]
,[4,4,4,2]]
,[[1,1,0,1]
,[2,3,2,1]
,[0,1,4,4]
,[3,1,1,4]]
,[[3,3,1,1]
,[0,0,1,1]
,[0,3,1,1]
,[0,4,3,4]]
,[[4,2,2,4]
,[0,1,0,1]
,[3,2,2,2]
,[4,1,3,4]]
,[[2,0,0,3]
,[1,0,1,3]
,[0,1,1,1]
,[4,2,0,3]]
,[[4,3,3,2]
,[1,0,0,1]
,[1,0,0,1]
,[0,4,4,3]]
,[[2,1,3,2]
,[1,1,4,0]
,[1,1,3,1]
,[1,0,0,3]]
,[[0,0,0,3]
,[3,3,0,4]
,[3,4,2,4]
,[3,2,2,2]]
,[[0,4,0,0]
,[2,2,0,2]
,[1,2,2,0]
,[2,1,0,0]]
,[[2,3,0,2]
,[0,3,2,0]
,[4,2,2,4]
,[0,3,0,3]]
,[[4,0,0,0]
,[4,3,2,1]
,[2,3,3,0]
,[4,1,1,2]]
,[[2,3,3,4]
,[4,4,3,2]
,[1,1,0,0]
,[1,2,3,2]]
,[[0,4,4,2]
,[3,4,4,4]
,[0,3,0,2]
,[1,4,3,4]]
,[[0,2,4,3]
,[3,4,4,4]
,[0,1,1,0]
,[0,1,4,1]]
,[[0,2,3,2]
,[4,0,1,2]
,[1,4,3,4]
,[4,4,0,0]]
,[[1,4,3,0]
,[2,4,1,3]
,[2,1,2,3]
,[2,3,2,3]]
,[[0,0,3,4]
,[2,0,2,3]
,[2,1,2,0]
,[2,2,3,4]]
,[[2,2,4,4]
,[4,1,1,1]
,[0,0,4,1]
,[3,0,0,1]]]
)
        C = {
            "OUTER_BOUNDARY": 6,
            "FULL_BLOCK": 12,
            "EL_SHAPE": 7
            }
        T = [18,19,16,17]

        result = main(l,C,T)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
