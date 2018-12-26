import numpy as np


def gradient_descent(x, y):
    m_curr = 0
    b_curr = 0
    epoch = 10000
    learning_rate = 0.001
    n = len(x)
    for i in range(epoch):
        ypred = m_curr * x + b_curr
        cost = (1 / n) * sum([i ** 2 for i in (y - ypred)])
        m_deravative = -(2 / n) * sum(x * (y - ypred))
        b_deravative = -(2 / n) * sum(y - ypred)

        m_curr = m_curr - learning_rate * m_deravative
        b_curr = b_curr - learning_rate * b_deravative

        print("m :{},b:{}, epoch :{},cost:{}".format(m_curr, b_curr, i, cost))


x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

gradient_descent(x, y)

