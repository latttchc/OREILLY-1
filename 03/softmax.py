import numpy as np

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) #指数関数の中では値の最大値を引く(overflow対策)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

