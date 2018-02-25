import tensorflow as tf
import sys
import os

sess = tf.InteractiveSession()

a = tf.Variable([1.0, 2.0])
b = tf.Variable([3.0, 4.0])

sess.run(tf.global_variables_initializer())

res = tf.add(a, b)
print(res.eval())


base_path = os.getcwd()
base_path = base_path[:base_path.find("python_study\\") + 13]
file_path = base_path + "dataMining\\deeplearning\\game\\"

sys.path.append(file_path)

print(sys.path)