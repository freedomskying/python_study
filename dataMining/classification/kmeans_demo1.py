from sklearn.datasets import load_iris

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

from sklearn.externals.six import StringIO
import pydotplus

import numpy as np

# 导入鸢尾花数据集
iris = load_iris()

# 切分预测集和测试集
test_idx = [0, 50, 100]

# training data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

# testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

# 默认函数构造决策树
clf = DecisionTreeClassifier()

clf = clf.fit(train_data, train_target)

print(test_target)
print(clf.predict(test_data))

cross_val_score(clf, iris.data, iris.target, cv=10)

# viz code 可视化 制作一个简单易读的PDF

dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("iris.pdf")
