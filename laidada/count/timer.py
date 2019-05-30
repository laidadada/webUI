# -*- encoding:utf-8 -*-

import time

def help():
    print('''我是一个计时器工具类，实现如下功能：
    1. 启动计时器:           start()
    2. 单次计时:             counter()
    3. 停止计时器            stop()
    4. 输出总耗时            output_total()
    5. 输出每个单次耗时      output_counter_times()
    6. 输出平均耗时          output_avg_time()
''')

total_cost_time = 0
counter_times = []
avg_cost_time = 0


start_time = 0
end_time = 0
def start():
    global start_time
    start_time = time.time()

def stop():
    global end_time
    end_time = time.time()

def counter():
    global counter_time
    current_time = time.time()
    counter_time = current_time - start_time
    counter_times.append(counter_time)

def output_total():
    total_cost_time = end_time - start_time
    print("总耗时：%s秒" % total_cost_time)

def output_counter_times():
    for i in range(0,len(counter_times)):
        print ("第%s计时，累计耗时%s秒" % ((i+1),counter_times[i]))

def output_avg_time(self):
    counter_len = len(counter_times)
    avg_cost_time = total_cost_time / float(counter_len)
    print ("平均耗时：%s秒" % avg_cost_time)

