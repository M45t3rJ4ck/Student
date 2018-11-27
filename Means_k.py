import pandas as pd
import numpy as np
from scipy.cluster.vq import kmeans, vq
import matplotlib.pyplot as plt


def reader_csv():
    df = pd.read_csv("data1953.csv")
    # df = pd.read_csv("data2008.csv")
    # df = pd.read_csv("dataBoth.csv")
    # labels = df["LifeExpectancy(1953)"]
    # labels = df["LifeExpectancy(2008)"]
    # labels = df["LifeExpectancy"]
    labels = df["BirthRate(Per1000 - 1953)"]
    # labels = df["BirthRate(Per1000 - 2008)"]
    # labels = df["BirthRate(Per1000)"]
    return df, labels


df, labels = reader_csv()
df = df.drop(["Countries"], axis=1)
data = np.array(df)

centroids, _ = kmeans(data, 2)
idx, _ = vq(data, centroids)
plt.plot(data[idx == 0, 0], data[idx == 0, 1], 'ob',
         data[idx == 1, 0], data[idx == 1, 1], 'or')
plt.plot(centroids[:, 0], centroids[:, 1], 'sg', markersize=8)
plt.show()
