import unittest
from multiplication_game import report_time

class ReportTimeTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_report_time(self):
        expected_dict = {
            60 : "1 min  0.00 sec",
            3600 : "1 hr  0 min  0.00 sec",
            360 : "6 min  0.00 sec",
            364 : "6 min  4.00 sec",
            364.23 :  "6 min  4.23 sec",
            364.233 : "6 min  4.23 sec",
            364.239 : "6 min  4.24 sec",
        }

        for k,v in expected_dict.items():
            self.assertEquals(report_time(k), v)


if __name__ == '__main__':
    unittest.main()
