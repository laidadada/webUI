# -*- encoding:utf-8 -*-

import unittest

from count.timer_c import Timer
import time

class TestTimer(unittest.TestCase):
    def setUp(self):
        print("我是setUp 方法, 会在每个用例前执行")
        print("我先实例化一个timer定时器")
        self.timer = Timer()


    def tearDown(self):
        print("tearDown 方法，会在每个用例前执行")
        print("我来释放timer定时器实例，确保每次用的都是新的")
        del self.timer


    def test_total_cost_time(self):
        exp_cost_time = 1
        self.timer = Timer()
        self.timer.start()
        time.sleep(1)
        self.timer.stop()
        act_cost_time = int(self.timer.total_cost_time)

        self.assertEqual(exp_cost_time, act_cost_time)

    def test_output_counter_times(self):
        self.timer.output_counter_times()
        exp_counter_times = 1
        act_counter_times = self.timer.output_counter_times
        self.assertEqual(exp_counter_times,act_counter_times)


if __name__ == '__main__':
    unittest.main()
