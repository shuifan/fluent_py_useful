import time
import tensorflow as tf

a = tf.random_normal((100, 100))
b = tf.random_normal((100, 500))
c = tf.matmul(a, b)
sess = tf.InteractiveSession()
begin_time = time.time()
print(sess.run(c))
print('用时 --> ' + str(time.time() - begin_time) + 's')