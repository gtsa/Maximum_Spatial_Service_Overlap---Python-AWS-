import numpy as np
import time
import random

order_list = []
for n in range(100):
    for i in range(1000):
        s = time.time()
        for m in range(15):
            test_input = [str(i + 1) + " " + str(n + 1)] + [" ".join([str(random.randint(1, i + 1)) for k in range(3)])
                                                            for l in range(n + 1)]
            _N, _M = test_input[0].split()
            N, M = int(_N), int(_M)
            input_limits_validation([N, M])
            P = []
            for j in range(1, M):
                _XYK = test_input[j].split()
                X, Y, K = list(map(int, (_XYK)))
                input_limits_validation([X, Y, K])
                P.append([X, Y, K])
        t = time.time()
        order_list.append([n + 1, i + 1, t - s])
order_list