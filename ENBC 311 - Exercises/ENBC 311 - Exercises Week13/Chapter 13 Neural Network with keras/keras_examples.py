import tensorflow as tf
from tensorflow import keras
import numpy as np

# Generate random data for linear regression
x_train = np.random.rand(80, 2).astype(np.float32)
y_train = 3 * x_train[:, 0] + 5 * x_train[:, 1] + 2

x_val = np.random.rand(20, 2).astype(np.float32)
y_val = 3 * x_val[:, 0] + 5 * x_val[:, 1] + 2

# Define the linear regression model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=[2]),
    keras.layers.Dense(2, activation='relu'),
    keras.layers.Dense(1)
])

# Compile the model
model.compile(optimizer='tf.keras.optimizers.Adam(0.1)', loss='mean_squared_error', metrics=['mse'])

# Train the model
history = model.fit(x_train, y_train, epochs=100, validation_data=(x_val, y_val))

# Evaluate the model on the test set
test_loss, test_mse = model.evaluate(x_val, y_val)
print('Test loss:', test_loss)
print('Test MSE:', test_mse)


# Predict new values using the model
new_x = np.array([[0.5, 0.6], [0.7, 0.8], [0.9, 0.1]], dtype=np.float32)
predictions = model.predict(new_x)
True_values = 3 * new_x[:, 0] + 5 * new_x[:, 1] + 2
# Print the predictions
print(predictions)
print(True_values)