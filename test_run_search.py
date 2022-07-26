from unittest import TestCase
from run_search import run_search
import heapq


class Test(TestCase):
    """unit testing on the function of selecting top three half-hour record and least continuous 1.5hr record"""
    def setUp(self) -> None:
        traffic_log_path = 'logs/traffic_log.txt'
        _, _, self.top_three, self.least_three = run_search(traffic_log_path)

    def test_run_search_top_three(self):
        """to test the searched timestamp is in the ground truth list"""
        top_three_record = ["2022-07-04T05:00:00", "2022-07-12T09:00:00", "2022-07-14T16:00:00"]
        while self.top_three:
            cc, tt = heapq.heappop(self.top_three)
            self.assertIn(tt, top_three_record), 'incorrect top three record'

    def test_run_search_least_time_window(self):
        """to test the searched three continuous half hour record is in the ground truth list"""
        least_time_window = ["2022-07-17T18:00:00", "2022-07-17T18:30:00", "2022-07-17T19:00:00"]
        for cc, tt in self.least_three:
            self.assertIn(tt, least_time_window), "incorrect least time widnow record"