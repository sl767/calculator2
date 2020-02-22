import unittest
import numpy as np
from Statistics.statistics import Statistics
import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        np.seed(9)
        randomData = []
        i = 1
        while i < 6:
            randomData.append(random.randint(1,100))
            i += 1
        pprint.pprint(randomData)
        self.testData = randomData
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)


if __name__ == '__main__':
    unittest.main()
