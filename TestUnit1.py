import UnitDefTest
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up for class"""
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        """Tear down for class"""

        print("===================================")
        out ={}
        for key, value in cls.all_results.items():
            for k, v in value.items():
                out[k] = str(v)
            print(value)

    def setUp(self):
        """Set up for test"""
        self.usain = UnitDefTest.Runner("Усэйн", 10)
        self.andrew = UnitDefTest.Runner("Андрей", 9)
        self.nick = UnitDefTest.Runner("Ник", 3)
        print("Set up for [" + self.shortDescription() + "]")

    def test_start_tour_1(self):
        """first run / первый забег"""
        print("id: " + self.id())
        tour = UnitDefTest.Tournament(90, self.usain, self.nick)
        results = tour.start()
        last_runner = list(results.values())
        self.assertTrue(last_runner[-1] == "Ник")
        self.all_results[self.shortDescription()] = results

    def test_start_tour_2(self):
        """second run / второй забег"""
        print("id: " + self.id())
        tour = UnitDefTest.Tournament(90, self.andrew, self.nick)
        results = tour.start()
        last_runner = list(results.values())
        self.assertTrue(last_runner[-1] == "Ник")
        self.all_results[self.shortDescription()] = results

    def test_start_tour_3(self):
        """third run / третий забег"""
        print("id: " + self.id())
        tour = UnitDefTest.Tournament(90, self.andrew, self.usain, self.nick)
        results = tour.start()
        last_runner = list(results.values())
        self.assertTrue(last_runner[-1] == "Ник")
        self.all_results[self.shortDescription()] = results


if __name__ == "__main__":
    unittest.main()
