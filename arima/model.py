# -*- coding: utf-8 -*-
# @Time    : 2019/12/8
# @Author  : cd
# @简介    : 
# @File    : model.py


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math


def eliminate(data_list):
    lo, up = np.percentile(data_list, 25), np.percentile(data_list, 75)
    iqr = up - lo
    for c in data_list:
        if c < lo - 3 * iqr or c > up + 3 * iqr:
            print c


def main():
    data = pd.read_csv("order.csv")
    cnt = data['cnt']
    h = [i % 24 for i in range(len(cnt))]
    data['hour'] = h
    for h in range(24):
        print h
        sub = data.loc[data['hour'] == h]['cnt']
        eliminate(sub)

    plt.plot(cnt)
    plt.show()


if __name__ == '__main__':
    main()
