import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Flatten, Dense
from sklearn.model_selection import train_test_split
import os

# Function to load and preprocess an image
def load_and_preprocess_image(image_path):
  image = tf.io.read_file(image_path)
  image = tf.image.decode_jpeg(image, channels=1)  # Convert to grayscale
  image = tf.image.resize(image, (128, 128))  # Resize to desired input size
  image = np.expand_dims(image, axis=0)  # Add a batch dimension for TF models
  return image

# Function to load multiple images and labels (replace with your data loading logic)
def load_data(data_dir, num_classes):
  images = []
  labels = []
  for class_index in range(num_classes):
    class_dir = os.path.join(data_dir, str(class_index))  # Assuming class folders
    for image_file in os.listdir(class_dir):
      image_path = os.path.join(class_dir, image_file)
      image = load_and_preprocess_image(image_path)
      label = np.array([class_index])  # One-hot encoding for a single class
      images.append(image)
      labels.append(label)
  return np.array(images), np.array(labels)

# Define hyperparameters (adjust as needed)
data_dir = 'photo-1565569995015-414d4ef36690.jpeg'  # Replace with your data directory
num_classes = 10  # Number of classes in your dataset
test_size = 0.2  # Proportion of data for validation
random_state = 42  # For reproducibility

# Load the data
X, y = load_data(data_dir, num_classes)

# Split the dataset
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=test_size, random_state=random_state)

# Define the deep network architecture (functional API for flexibility)
inputs = tf.keras.Input(shape=(128, 128, 1))
x = Flatten()(inputs)
x = Dense(256, activation='sigmoid')(x)  # Hidden layer with sigmoid activation
outputs = Dense(num_classes, activation='softmax')(x)  # Output layer with softmax activation

model = tf.keras.Model(inputs=inputs, outputs=outputs)

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))

# Evaluate the model
loss, accuracy = model.evaluate(X_val, y_val)
print(f"Validation loss: {loss}")
print(f"Validation accuracy: {accuracy}")



# In summary, this code demonstrates the process of 
# building, training, and evaluating a deep learning model for image classification using TensorFlow and Keras.