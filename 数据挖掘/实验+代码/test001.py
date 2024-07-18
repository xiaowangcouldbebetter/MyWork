# -*- coding:gb2312 -*-
import sys
import copy

# 初始化数据集的第一次遍历
def init_pass(T):
    C = {}  # 创建一个空字典C
    for t in T:  # 对于数据集中的每一个事务
        for i in t:  # 对于事务中的每一个项
            if i in C.keys():  # 如果项已经在字典C中
                C[i] += 1  # 则计数加1
            else:  # 否则
                C[i] = 1  # 将该项加入字典C，并初始化计数为1
    return C  # 返回计数后的字典C

# 生成候选项集
def generate(F):
    C = []  # 创建一个空列表C
    k = len(F[0]) + 1  # 获取F中项集的长度
    for f1 in F:  # 对于F中的每一个项集f1
        for f2 in F:  # 对于F中的每一个项集f2
            if f1[k-2] < f2[k-2]:  # 如果f1的前k-2个项与f2的前k-2个项相同
                c = copy.copy(f1)  # 将f1复制给c
                c.append(f2[k-2])  # 将f2的第k-2个项添加到c中
                flag = True  # 初始化标志为True
                for i in range(0, k-1):  # 对于c中的每一个项
                    s = copy.copy(c)  # 复制c给s
                    s.pop(i)  # 移除s中的第i个项
                    if s not in F:  # 如果s不在F中
                        flag = False  # 则将标志设置为False
                        break  # 跳出循环
                if flag and c not in C:  # 如果标志为True且c不在C中
                    C.append(c)  # 将c添加到C中
    return C  # 返回候选项集C

# 比较两个列表
def compareList(A, B):
    if len(A) <= len(B):  # 如果A的长度小于等于B的长度
        for a in A:  # 对于A中的每一个项
            if a not in B:  # 如果a不在B中
                return False  # 则返回False
    else:  # 否则
        for b in B:  # 对于B中的每一个项
            if b not in A:  # 如果b不在A中
                return False  # 则返回False
    return True  # 否则返回True

# Apriori算法
def apriori(T, minSupport):
    D = []  # 创建一个空列表D
    C = init_pass(T)  # 对数据集进行初始化遍历，得到计数字典C

    keys = sorted(C)  # 对C中的键进行排序
    D.append(keys)  # 将排序后的键加入D集中
    F = [[]]  # 创建一个空列表F
    for f in D[0]:  # 对于D中的每一个项
        if C[f] >= minSupport:  # 如果该项的计数大于等于最小支持度
            F[0].append([f])  # 则将该项添加到F中
    k = 1  # 初始化k为1

    while F[k-1] != []:  # 当F[k-1]不为空时
        D.append(generate(F[k-1]))  # 生成候选项集D[k]
        F.append([])  # 将F[k]初始化为空列表
        for c in D[k]:  # 对于D[k]中的每一个项集c
            count = 0  # 初始化计数为0
            for t in T:  # 对于数据集中的每一个事务
                if compareList(c, t):  # 如果c是事务t的子集
                    count += 1  # 则计数加1
            if count >= minSupport:  # 如果计数大于等于最小支持度
                F[k].append(c)  # 则将c添加到F[k]中
        k += 1  # k加1

    U = []  # 创建一个空列表U
    for f in F:  # 对于F中的每一个项集f
        for x in f:  # 对于f中的每一个项x
            U.append(x)  # 将x添加到U中
    return U  # 返回频繁项集U

# 数据集
T = [['A', 'C', 'D'], ['B', 'C', 'E'], ['A', 'B', 'C', 'E'], ['B', 'E']]

# 调用Apriori算法
Z = apriori(T, 2)
print(Z)  # 打印频繁项集Z
