from numpy import *
import time
import matplotlib.pyplot as plt
import KMeans

## step 1: load data  
print("step 1: load data...")
dataSet = []  # 列表，用来表示，列表中的每个元素也是一个二维的列表；这个二维列表就是一个样本，样本中包含有我们的属性值和类别号。
# 与我们所熟悉的矩阵类似，最终我们将获得N*2的矩阵，每行元素构成了我们的训练样本的属性值和类别号
fileIn = open("./code.vec")  # 是正斜杠
dic = dict()
j = 0
for line in fileIn.readlines():
    temp = []
    lineArr = line.strip().split(' ')  # line.strip()把末尾的'\n'去掉
    for i in range(0, 200):
        temp.append(float(lineArr[i]))
    dataSet.append(temp)
    dic[j] = temp
    j = j + 1
fileIn.close()
#####for key in dic:
#####    print(key, dic[key])
## step 2: clustering...  
print("step 2: clustering...")
#print(dataSet)
dataSet = mat(dataSet)  # mat()函数是Numpy中的库函数，将数组转化为矩阵
#print(dataSet)

k = 5
centroids, clusterAssment = KMeans.kmeans(dataSet, k, dic)  # 调用KMeans文件中定义的kmeans方法。

## step 3: show the result  
print("step 3: show the result...")
KMeans.showCluster(dataSet, k, centroids, clusterAssment)

### i其实就是每个code vec 的id; 具体的数据在dateSet[i]中;
for i in range(0, len(clusterAssment)):
    print(i, '   ', clusterAssment[i, 0])