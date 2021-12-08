# coding: utf-8

"""
时间复杂度：
    每次 O(LogN) 
    第一次重建权重表复杂度 O(N)

过程：

1、重建权重表，列表中每个权重是前面所有权重值的总和，得到有序权重表

2、先计算出所有道具的权重总和S，

3、然后调用随机函数得到一个区间在[1, S]的随机值N

4、根据N在有序权重表二分查找
"""

import random
import pysnooper


def binary_random(pool_data):
    add = 0
    pool = []  # [(1, 50), (2, 70), (3, 110), (4, 120)]
    for k, w in pool_data:
        add += w
        pool.append((k, add))

    sum_weight = pool[-1][1]
    n = random.randint(1, sum_weight)
    mid, left, right, = 0, 0, len(pool) - 1
    while left < right:  # 二分查找
        mid = (right + left) // 2
        key, mid_num = pool[mid]
        if mid_num < n:
            left = mid + 1
        elif mid_num > n:
            right = mid
        else:
            return key
    return pool[right][0]


def test():
    # 测试数据 [(奖励ID: 权重)]
    pool_data = [
        (1, 50),
        (2, 20),
        (3, 40),
        (4, 10),
    ]
    print(binary_random(pool_data))


if __name__ == "__main__":
    test()
