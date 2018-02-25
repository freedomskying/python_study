import tensorflow as tf

mat1 = tf.constant(([[3., 3.]]))  # 创建一个1*2的矩阵
mat2 = tf.constant(([[2.], [2.]]))  # 创建一个2*1的矩阵

product = tf.matmul(mat1, mat2)  # 创建op执行两个矩阵的乘法
sess = tf.Session()  # 启动默认图
res = sess.run(product)  # 在默认图中执行op操作

print(res)
sess.close()
