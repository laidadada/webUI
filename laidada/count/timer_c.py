# -*- encoding:utf-8 -*-

import time

class Timer():
    __total_cost_time = 0
    __counter_times = []
    __avg_cost_time = 0
    __start_time = 0
    __end_time = 0

    def start(self):
        self.__start_time = time.time()

    def stop(self):
        self.__end_time = time.time()

    def counter(self):
        current_time = time.time()
        counter_time = current_time - self.__start_time
        self.__counter_times.append(counter_time)

    @property
    def total_cost_time(self):
        self.__total_cost_time = self.__end_time - self.__start_time
        return self.__total_cost_time


    def output_total(self):
        self.__total_cost_time = self.__end_time - self.__start_time
        print (self.__total_cost_time)

    def output_counter_times(self):
        for i in range(0, len(self.__counter_times)):
            print ("第%s计时，累计耗时%s秒" % ((i + 1), self.__counter_times[i]))

    def output_avg_time(self):
        counter_len = len(self.__counter_times)
        avg_cost_time = self.__total_cost_time / float(counter_len)
        print ("平均耗时：%s秒" % avg_cost_time)