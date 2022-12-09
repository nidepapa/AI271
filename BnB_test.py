import time

import BnB

if __name__ == "__main__":
    costMatrix1 = [[float("inf"), 11.8658, 14.0778, 4.2337, 1.4596],
                  [11.8658, float("inf"), 10.2788, 6.3823, 13.3265],
                  [14.0778, 10.2788, float("inf"), 4.0575, 17.2087],
                  [4.2337, 6.3823, 4.0575, float("inf"), 28.0986],
                  [1.4596, 13.3265, 17.2087, 28.0986, float("inf")]]

    costMatrix2 = [[float("inf"), 0.5303, 0.1727, 2.7942, 2.3385, 1.9787, 0.6226, 0.7087, 1.3965, 0.7403],
                   [0.5303, float("inf"), 1.6619, 1.7715, 0.3817, 0.5030, 0.0054, 0.3665, 1.0130, 0.9184],
                   [0.1727, 1.6619, float("inf"), 0.0881 ,1.3253, 1.5245, 0.9192, 1.8067, 0.4636, 0.8676],
                   [2.7942, 1.7715, 0.0881, float("inf"), 1.2906, 1.7981, 0.2393, 0.0672, 0.8743, 1.1939],
                   [2.3385, 0.3817, 1.3253, 1.2906, float("inf"), 0.3020, 0.7884, 0.0550, 0.5590, 1.3183],
                   [1.9787, 0.5030, 1.5245, 1.7981, 0.3020, float("inf"), 1.0629, 0.6247, 1.6497, 0.4459],
                   [0.6226, 0.0054,0.9192, 0.2393, 0.7884, 1.0629, float("inf"), 0.5316, 0.4628, 0.7779],
                   [0.7087, 0.3665, 1.8067, 0.0672, 0.0550, 0.6247, 0.5316, float("inf"), 1.3560, 0.0458],
                   [1.3965, 1.0130, 0.4636, 0.8743, 0.5590, 1.6497, 0.4628, 1.3560, float("inf"), 0.7441],
                   [0.7403, 0.9184, 0.8676, 1.1939, 1.3183, 0.4459, 0.7779, 0.0458, 0.7441, float("inf")]]

    start = time.time()
    for i in range(10000):
        cost, expending = BnB.BnB_DFS_TSP(costMatrix1)
    end = time.time()
    print('Running time: %s Seconds' % (end - start))
    print('cost of the tour:', cost)
    print('number of expanding nodes:', expending)

    start = time.time()
    for i in range(10000):
        cost, expending = BnB.BnB_DFS_TSP(costMatrix2)
    end = time.time()
    print('Running time: %s Seconds' % (end - start))
    print('cost of the tour:', cost)
    print('number of expanding nodes:', expending)
