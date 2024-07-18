# -*- coding:gb2312 -*-
import sys
import copy

# ��ʼ�����ݼ��ĵ�һ�α���
def init_pass(T):
    C = {}  # ����һ�����ֵ�C
    for t in T:  # �������ݼ��е�ÿһ������
        for i in t:  # ���������е�ÿһ����
            if i in C.keys():  # ������Ѿ����ֵ�C��
                C[i] += 1  # �������1
            else:  # ����
                C[i] = 1  # ����������ֵ�C������ʼ������Ϊ1
    return C  # ���ؼ�������ֵ�C

# ���ɺ�ѡ�
def generate(F):
    C = []  # ����һ�����б�C
    k = len(F[0]) + 1  # ��ȡF����ĳ���
    for f1 in F:  # ����F�е�ÿһ���f1
        for f2 in F:  # ����F�е�ÿһ���f2
            if f1[k-2] < f2[k-2]:  # ���f1��ǰk-2������f2��ǰk-2������ͬ
                c = copy.copy(f1)  # ��f1���Ƹ�c
                c.append(f2[k-2])  # ��f2�ĵ�k-2������ӵ�c��
                flag = True  # ��ʼ����־ΪTrue
                for i in range(0, k-1):  # ����c�е�ÿһ����
                    s = copy.copy(c)  # ����c��s
                    s.pop(i)  # �Ƴ�s�еĵ�i����
                    if s not in F:  # ���s����F��
                        flag = False  # �򽫱�־����ΪFalse
                        break  # ����ѭ��
                if flag and c not in C:  # �����־ΪTrue��c����C��
                    C.append(c)  # ��c��ӵ�C��
    return C  # ���غ�ѡ�C

# �Ƚ������б�
def compareList(A, B):
    if len(A) <= len(B):  # ���A�ĳ���С�ڵ���B�ĳ���
        for a in A:  # ����A�е�ÿһ����
            if a not in B:  # ���a����B��
                return False  # �򷵻�False
    else:  # ����
        for b in B:  # ����B�е�ÿһ����
            if b not in A:  # ���b����A��
                return False  # �򷵻�False
    return True  # ���򷵻�True

# Apriori�㷨
def apriori(T, minSupport):
    D = []  # ����һ�����б�D
    C = init_pass(T)  # �����ݼ����г�ʼ���������õ������ֵ�C

    keys = sorted(C)  # ��C�еļ���������
    D.append(keys)  # �������ļ�����D����
    F = [[]]  # ����һ�����б�F
    for f in D[0]:  # ����D�е�ÿһ����
        if C[f] >= minSupport:  # �������ļ������ڵ�����С֧�ֶ�
            F[0].append([f])  # �򽫸�����ӵ�F��
    k = 1  # ��ʼ��kΪ1

    while F[k-1] != []:  # ��F[k-1]��Ϊ��ʱ
        D.append(generate(F[k-1]))  # ���ɺ�ѡ�D[k]
        F.append([])  # ��F[k]��ʼ��Ϊ���б�
        for c in D[k]:  # ����D[k]�е�ÿһ���c
            count = 0  # ��ʼ������Ϊ0
            for t in T:  # �������ݼ��е�ÿһ������
                if compareList(c, t):  # ���c������t���Ӽ�
                    count += 1  # �������1
            if count >= minSupport:  # ����������ڵ�����С֧�ֶ�
                F[k].append(c)  # ��c��ӵ�F[k]��
        k += 1  # k��1

    U = []  # ����һ�����б�U
    for f in F:  # ����F�е�ÿһ���f
        for x in f:  # ����f�е�ÿһ����x
            U.append(x)  # ��x��ӵ�U��
    return U  # ����Ƶ���U

# ���ݼ�
T = [['A', 'C', 'D'], ['B', 'C', 'E'], ['A', 'B', 'C', 'E'], ['B', 'E']]

# ����Apriori�㷨
Z = apriori(T, 2)
print(Z)  # ��ӡƵ���Z
