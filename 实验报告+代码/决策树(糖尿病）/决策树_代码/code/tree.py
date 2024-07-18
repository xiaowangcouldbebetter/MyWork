
#导入库
import matplotlib.pyplot as plt
from math import log
import pandas as pd
import operator
import pickle
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']        # 配置字体，使其支持中文显示

#定义决策节点、子叶节点、见图的样式
decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")

def getDataSet():
    data = pd.read_csv("../data/diabetes_data.csv") # 获取数据集（定义函数：获取目标路径下的数据）        #read_csv读取纯文本文件,对数据预处理
    # 去掉Age列
    data = data.drop(columns=['Age'], axis=1)
    # 将所有No/Yes分别转换为0/1，便于后面决策树的创建
    data['Gender'][data["Gender"] == 'Male'] = 1
    data['Gender'][data["Gender"] == 'Female'] = 0

    #利用循环将数据中的no\yes转换为0或1
    for i in data.columns:
        data[i][data[i] == 'No'] = 0
        data[i][data[i] == 'Yes'] = 1
    # 取前410个数据作为测试数据（共520个）
    data = data[:][:410]
    # print(data.shape)
    dataSet = data.values.tolist()                   #将处理后的数据集转换成列表形式，以便于后续使用
    # 属性标签，包含糖尿病数据据中的各个属性名称
    labels = ['Gender','Polyuria', 'Polydipsia', 'sudden weight loss','weakness','Polyphagia','Genital thrush', 'visual blurring','Itching',
              'Irritability','delayed healing', 'partial paresis', 'muscle stiffness','Alopecia','Obesity']
    return dataSet, labels

# 统计classCount中出现此处最多的元素
def majorityCnt(classList):
    classCount = {}                                   #创建一个字典

    #对每个类进行遍历，并对元素进行判断是否咋字典中，不在便赋值为0加入字典
    for vote in classList:
        if vote not in classCount.keys():
            classList[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]#返回出现次数最多的类别

# 计算数据集的香农熵
def calcShannonEnt(dataSet): 
    numEntires = len(dataSet)                           #返回数据集的行数
    labelCounts = {}                                    #保存每个标签(Label)出现次数的字典
    for featVec in dataSet:                             #对每组特征向量进行统计
        currentLabel = featVec[-1]                      #提取标签(Label)信息
        if currentLabel not in labelCounts.keys():      #如果标签(Label)没有放入统计次数的字典,添加进去
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1                  #Label计数
        shannonEnt = 0.0                                #经验熵(香农熵)
        for key in labelCounts:                         #计算香农熵
            prob = float(labelCounts[key]) / numEntires #选择该标签(Label)的概率
            shannonEnt -= prob * log(prob, 2)           #利用公式计算
    return shannonEnt                                   #返回经验熵(香农熵)

# 按照给定特征划分数据集
def splitDataSet(dataSet, axis, value):
    retDataSet = []                                     #创建返回的数据集列表
    for featVec in dataSet:                             #遍历数据集
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]             #去掉axis特征
            reducedFeatVec.extend(featVec[axis+1:])     #将符合条件的添加到返回的数据集
            retDataSet.append(reducedFeatVec)
    return retDataSet                                   #返回划分后的数据集

# 获取最优特征值
def chooseBestFeatureToSplit(dataSet):
    numFeature = len(dataSet[0]) - 1                    # 特征值数量
    baseEntropy = calcShannonEnt(dataSet)               # 计算数据集的香农熵
    # print(baseEntropy)
    bestInfoGain = 0.0  # 信息增益
    bestFeature = -1
    for i in range(numFeature):
        #获取dataSet的第i个所有特征
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)        #创建set集合{},元素不可重复
        newEntropy = 0.0                  #经验条件熵
        for value in uniqueVals:          #计算信息增益
            subDataSet = splitDataSet(dataSet, i, value)       #subDataSet划分后的子集
            prob = len(subDataSet) / float(len(dataSet))  # 计算子集的概率
            newEntropy += prob * calcShannonEnt(subDataSet)  # 根据公式计算经验条件熵
        infoGain = baseEntropy - newEntropy  # 信息增益
        # print("第%d个特征的增益为%.3f" % (i, infoGain))			# 打印每个特征的信息增益
        if (infoGain > bestInfoGain):  # 计算信息增益
            bestInfoGain = infoGain  # 更新信息增益，找到最大的信息增益
            bestFeature = i  # 记录信息增益最大的特征的索引值
    return bestFeature

# 创建决策树
def createTree(dataSet, labels, featLabels):
    classList = [example[-1] for example in dataSet]          #取分类标签(是否患糖尿病:positive or negative)
    # print(classList)
    if classList.count(classList[0]) == len(classList):       #如果类别完全相同则停止继续划分
        return classList[0] 
    if len(dataSet[0]) == 1 or len(labels) == 0:              #遍历完所有特征时返回出现次数最多的类标签 
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)              #选择最优特征
    # print(bestFeat)
    bestFeatLabel = labels[bestFeat]
    featLabels.append(bestFeatLabel)
    myTree = {bestFeatLabel:{}}                            #根据最优特征的标签生成树
    del(labels[bestFeat])                                  #删除已经使用特征标签
    featValues = [example[bestFeat] for example in dataSet]#得到训练集中所有最优特征的属性值
    uniqueVals = set(featValues)                           #去掉重复的属性值
    # print(uniqueVals)
    for value in uniqueVals:                               #遍历特征，创建决策树。
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels, featLabels)
    return myTree

# 绘制结点
def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction', \
                            xytext=centerPt, textcoords='axes fraction', \
                            va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)

# 获取树的叶子数量
def getNumLeafs(myTree):
    numLeafs = 0                        #定义叶子
    firstStr = list(myTree.keys())[0]# 获取第一个键值key
    secondDict = myTree[firstStr]

    # 通过遍历遍历当前节点的所有子节点，如果子节点是字典类型，则说明该节点不是叶子节点，需要继续递归遍历其子树，否则，说明该节点是叶子节点，将叶子数量加1
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs

# 获取树的深度
# 通过递归进行深度遍历，计算每个节点所在的深度，然后取所有节点深度的最大值作为整棵树的深度。
def getTreeDepth(myTree):
    maxDepth = 0         # 定义变量深度的最大值，初始值为0
    firstStr = list(myTree.keys())[0]# 选取字典的第一个值，获取当前节点的信息
    secondDict = myTree[firstStr]
# 遍历 secondDict 中的每个子节点
    for key in secondDict.keys():
        # 如果该子节点也是一个字典，则递归调用 getTreeDepth 函数来获取其深度，并将得到的深度值加上1。不是字典类型，则说明它是一个叶节点，深度为 1。
        if type(secondDict[key]).__name__ == 'dict':
            thisDepth = getTreeDepth(secondDict[key]) + 1
        else:
            thisDepth = 1
        # 如果 thisDepth 大于 maxDepth，则将 maxDepth 更新为 thisDepth。
        if thisDepth > maxDepth:
            maxDepth = thisDepth
    return maxDepth
# 标注有向边属性值
def plotMidText(cntrPt, parentPt, txtString):
    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString)

# 绘制决策树
def plotTree(myTree, parentPt, nodeTxt):
    numLeafs = getNumLeafs(myTree)  # 树的叶子数量
    depth = getTreeDepth(myTree)  # 树的深度
    firstStr = list(myTree.keys())[0]  # 取树（字典）的第一个元素
    # 计算当前节点的位置坐标
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs)) / 2.0 / plotTree.totalw, plotTree.yOff)
    # 在父子节点间填充文本信息--绘制线上的文字
    plotMidText(cntrPt, parentPt, nodeTxt)
    # 绘制带箭头的注解--节点
    plotNode(firstStr, cntrPt, parentPt, decisionNode)
    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD
    #如果当前节点是非叶节点，则递归调用plotTree函数进行绘制。如果当前节点是叶节点，则绘制叶节点并填充文本信息。
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            plotTree(secondDict[key], cntrPt, str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0 / plotTree.totalw
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0 / plotTree.totalD


# 创建决策树画板
def createPlot(inTree):
    fig = plt.figure(figsize=(12, 8), facecolor='white')  # 创建画布
    fig.clf()  # 清屏
    axprops = dict(xticks=[], yticks=[])
    # print(axprops)
    # 创建一个1行1列1figure,并把网格里面的第一个figure的Axes实例返回给ax1作为函数createPlot()的属性，这个属性ax1相当于一个全局变量，可以给plotNode函数使用
    createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)
    plotTree.totalw = float(getNumLeafs(inTree))  # 叶子节点的数量
    plotTree.totalD = float(getTreeDepth(inTree))  # 树的深度
    # 节点的x轴的偏移量为 - 1 / plotTree.totlaW / 2, 1为x轴的长度，除以2保证每一个节点的x轴之间的距离为1/plotTree.totlaW*2
    plotTree.xOff = -0.5 / plotTree.totalw
    plotTree.yOff = 1.0
    plotTree(inTree, (0.5, 1.0), '')
    plt.title("决策树", fontsize=12, color='r')
    plt.show()

# 验证数据集
def classify(myTree, featLabels, testVec):
    firstStr = next(iter(myTree))       #获取决策树结点
    secondDict = myTree[firstStr]          #下一个
    featIndex = featLabels.index(firstStr)
    classLabel = 'p'
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featLabels, testVec)
            else:
                classLabel = secondDict[key]
    return classLabel


def modelTest(myTree, featLabels):
    # 取后109个数据作为测试集
    data = pd.read_csv("../data/diabetes_data1.csv")
    data = data[:][411:]
    classList = [data['class'][i+411] for i in range(data.shape[0])]#
    # print(data)
    testVec = []      #存储测试数据对应的featLabels属性集的值
    for (j) in range(data.shape[0]):
        mod = []
        for i in featLabels:
            mod.append(data[i][j+411])
        testVec.append(mod)
    result = []
    count = 0
    for i in range(109):        #验证数据
        res = classify(myTree, featLabels, testVec[i])#调用 classify 函数进行分类预测，将预测结果与真实标签比较，统计分类错误的数量
        if res != classList[i]:
            count += 1
    print("模型准确率：%.4f" %((109-count)/float(109)))     # 计算模型准确率

if __name__ == '__main__':
    # 获取数据集
    dataSet, labels = getDataSet()
    featLabels = []
    # 创建ID3决策树
    myTree = createTree(dataSet, labels, featLabels)
    print(featLabels)
    print(myTree)
    # 绘制决策树
    createPlot(myTree)
    # 模型测试
    modelTest(myTree, featLabels)
