# K-Means clustering implementation
# Some hints on how to start have been added to this file.
# You will have to add more code that just the hints provided here for the full implementation.
# ====
import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np


# Define a function that computes the distance between two data points
# ====
class Point:

    def __init__(self, point_1, point_2):
        self.point1 = point_1
        self.point2 = point_2

    def distance(self):
        dist = math.sqrt(math.pow(self.point_1[0] - self.point_2[0], 2.0) + math.pow(self.point_1[0] - self.point_2[0], 2.0))
        return dist


# Define a function that reads data in from the csv files
def csv_read():
    df_1953 = pd.read_csv("data1953.csv")
    # df_2008 = pd.read_csv("data2008.csv")
    # df_both = pd.read_csv("dataBoth.csv")
    # classes_l = df_both["LifeExpectancy"]
    classes_b = df_1953["BirthRate(Per1000 - 1953)"]
    return df_1953, classes_b
# ====

# Write the initialisation procedure

# ====


# Implement the k-means algorithm, using appropriate looping
df_1953, classes_b = csv_read()
df = df_1953.drop(["Countries"], axis=1)
data = df.values.tolist()
data = np.array(data)
train_data = data[:147]
test_data = data[147:]

# ====
# Print out the results
plt.xlabel("Countries")
plt.ylabel("Birth Rate (Per1000)")
plt.title("1953")
plt.plot(data, "bs")
plt.grid(True)
plt.show()
