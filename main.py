import matplotlib.pyplot as plt
import random
import math

theta = 1
n = 1000
s = 1000


def uniform(k):
    sum = 0
    for _ in range(n):
        sum += random.uniform(0, theta) ** k
    return ((k + 1) * (sum / n)) ** (1.0 / k)


def exp(k):
    sum = 0
    for _ in range(n):
        sum += random.expovariate(theta) ** k
    return ((sum / n) / math.factorial(k)) ** (1.0 / k)


def calculate_sko(k, fun):
    return sum([(theta - fun(k)) ** 2 for _ in range(s)]) / s


def draw(path, fun):
    count = 150
    points = []
    for k in range(1, count):
        points.append(calculate_sko(k, fun))
    plt.clf()
    plt.plot([i for i in range(1, count)], points)
    plt.savefig(path)


draw("uni.png", uniform)
draw("exp.png", exp)
