# -*- encoding:utf-8 -*-

from count import timer

import time

#开启计时器
timer.start()

#休眠500毫秒，运行3次
for i in range(3):
    time.sleep(0.5)
    timer.counter()

#停止计时器
timer.stop()

#输出总耗时
timer.output_total()
timer.output_counter_times()