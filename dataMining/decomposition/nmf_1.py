# 导入随机种子
from numpy.random import RandomState
import matplotlib.pyplot as plt
# 导入Olivetti图像
from sklearn.datasets import fetch_olivetti_faces
from sklearn import decomposition

# 非负矩阵分解 Non-negative Matrix Fatorization

# 设置2*3图相框，制定图像排列情况，2行3列
n_row, n_col = 2, 3
n_components = n_row * n_col

# 设置提取特征的数目为64*64
image_shape = (64, 64)

###############################################################################
# Load faces data
# 使用随机种子打乱顺序，每次运行程序出现的图像和特征都不一样
dataset = fetch_olivetti_faces(shuffle=True, random_state=RandomState(0))
faces = dataset.data

###############################################################################
def plot_gallery(title, images, n_col=n_col, n_row=n_row):
    # 创建图片，并且制定图片的大小
    plt.figure(figsize=(2. * n_col, 2.26 * n_row))
    # 设置标题及字号大小
    plt.suptitle(title, size=16)

    for i, comp in enumerate(images):
        # 选择画制的子图
        plt.subplot(n_row, n_col, i + 1)

        vmax = max(comp.max(), -comp.min())

        # 对数据归一化，并以灰度图形式展示
        plt.imshow(comp.reshape(image_shape), cmap=plt.cm.gray,
                   interpolation='nearest', vmin=-vmax, vmax=vmax)

        # 去除子图的坐标轴标签，对子图的间隔位置进行调整；
        plt.xticks(())
        plt.yticks(())
    plt.subplots_adjust(0.01, 0.05, 0.99, 0.94, 0.04, 0.)


plot_gallery("First centered Olivetti faces", faces[:n_components])
###############################################################################

# 将PCA 和 NMF算法实例化，放入枚举中
estimators = [
    ('Eigenfaces - PCA using randomized SVD',
     decomposition.PCA(n_components=6, whiten=True)),

    ('Non-negative components - NMF',
     decomposition.NMF(n_components=6, init='nndsvda', tol=5e-3))
]

###############################################################################

# 分别调用PCA和NMF
for name, estimator in estimators:
    print("Extracting the top %d %s..." % (n_components, name))
    print(faces.shape)
    # 调用PCA或NMF提取特征
    estimator.fit(faces)
    components_ = estimator.components_
    # 按照固定格式进行排列
    plot_gallery(name, components_[:n_components])

plt.show()
