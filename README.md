# Handwritten Digit Recognition with Deep Learning

This project leverages deep learning techniques to classify handwritten digits using the **MNIST** dataset. A custom neural network model is designed using **Keras** with several advanced techniques such as regularization, batch normalization, and dropout to improve performance and generalization.


## Project Overview

This project involves building a deep neural network to recognize handwritten digits (0-9) from the MNIST dataset. The model uses several techniques, such as regularization, dropout, and batch normalization, to achieve better accuracy and prevent overfitting.

Key features:
- **Data Preprocessing**: The images are resized, normalized, and flattened to fit the model input.
- **Advanced Model Architecture**: The model consists of multiple dense layers with L2 regularization, dropout, and batch normalization to prevent overfitting and improve performance.
- **Training Optimization**: Early stopping and learning rate reduction callbacks are used to optimize training.

## Technologies Used

- **Python**: The primary programming language used in the project.
- **TensorFlow/Keras**: Framework used to build and train the deep learning model.
- **NumPy**: Used for numerical operations on data.
- **Matplotlib**: Used for visualizing model predictions and results.
- **PIL**: Python Imaging Library used for preprocessing images.
- **Tkinter**: GUI library used to create a simple drawing interface for testing the model.

## Usage

To use the model for digit classification, follow these steps:

1. **Run the GUI**: This interface allows you to draw digits, save the image, and predict the digit.
2. **Draw a Digit**: Use the drawing interface to draw a digit on the canvas.
3. **Predict the Digit**: Click the **Predict** button to predict the digit using the trained model.
4. **Save the Image**: The image is saved as `image_trial.png` in the working directory.

The model will predict the digit, and the result will be displayed on the interface, along with the corresponding image.
