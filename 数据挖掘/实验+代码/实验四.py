
#实验四：请利用利用sklearn库实现关联规则挖掘算法

# 导入所需的库
import sys
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# 定义Apriori算法函数
def apriori_algorithm(dataset_file, min_support, min_confidence):
    # 从csv文件中读取数据，数据是一个列表的列表，每个内部列表代表一个交易
    dataset = pd.read_csv(dataset_file, header=None).values.tolist()

    # 将所有的数字转换成字符串，这样就可以比较所有的项了
    dataset = [[str(item) for item in transaction] for transaction in dataset]

    # 使用TransactionEncoder将交易数据转换为一个布尔值的数据框
    # 这个数据框的每一行代表一个交易，每一列代表一个项，如果一个交易包含一个项，那么对应的值就是True，否则就是False
    te = TransactionEncoder()
    te_ary = te.fit(dataset).transform(dataset)
    df = pd.DataFrame(te_ary, columns=te.columns_)

    # 使用apriori找出频繁项集，频繁项集是在交易数据中出现频率超过最小支持度的项的集合
    frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)

    # 使用association_rules找出关联规则，关联规则是形如{A} -> {B}的规则，表示如果一个交易包含A，那么它很可能也包含B
    # 这里使用的度量是置信度，置信度是A和B同时出现的概率除以A出现的概率
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)

    # 打印找到的关联规则
    print(rules)


def main():
    # 检查命令行参数的数量，如果参数数量不对，就打印使用说明并退出
    if len(sys.argv) != 4:
        print("Usage: python apriori.py <dataset.csv> <minSup> <minConf>")
        return

    # 从命令行参数中获取数据集文件名、最小支持度和最小置信度
    dataset_file = sys.argv[1]
    min_support = float(sys.argv[2])
    min_confidence = float(sys.argv[3])

    # 调用Apriori算法
    apriori_algorithm(dataset_file, min_support, min_confidence)

# 如果这个脚本是直接运行的，而不是被导入的，那么就调用main函数
if __name__ == "__main__":
    main()
