import tensorflow as tf


w= tf.Variable([-0.05],dtype=tf.float32)
b= tf.Variable([0.05],dtype=tf.float32)

x=tf.placeholder(dtype=tf.float32)
y=tf.placeholder(dtype=tf.float32)

x_training = [1,2,3,4,5]
y_training = [6,7,8,9,10]

x_testing= [6,7,8,25]
# approximately obtain y as [-4,-5,-6,-7]

#the obtained values
linear_model = w * x + b
loss = tf.reduce_sum(tf.square(linear_model - y))
optimiser= tf.train.GradientDescentOptimizer(0.01)
#0.01 is learning rate of the model
#Gradient descent algorithm is used to minimize the loss
train=optimiser.minimize(loss)

session=tf.Session()
init=tf.global_variables_initializer()
session.run(init)

print(session.run(linear_model,{x:x_training}))
print(session.run(loss,{x:x_training,y:y_training}))

for i in range(10000):
    session.run(train,{x:x_training,y:y_training})

w,b,loss=session.run([w,b,loss],{x:x_training,y:y_training})
print(w)
print(b)
print(loss)

print(session.run(linear_model,{x:x_testing}))




