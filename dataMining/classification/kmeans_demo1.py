from sklearn.datasets import load_iris

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

#默认函数构造决策树
clf = DecisionTreeClassifier()

#导入鸢尾花数据集
iris = load_iris()

cross_val_score(clf, iris.data, iris.target, cv = 10)

