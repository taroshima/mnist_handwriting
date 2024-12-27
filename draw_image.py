from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageDraw, ImageOps
import numpy as np
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

class DrawingApp:
    def __init__(self, root, model):
        self.root = root
        self.root.title("Draw a Digit")
        self.model = model
        
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 10), padding=6)
        
        self.canvas = tk.Canvas(root, width=280, height=280, bg='#d3d3d3')
        self.canvas.pack(pady=10)
        
        self.button_save = ttk.Button(root, text="Predict", command=self.save_and_predict)
        self.button_save.pack(side=tk.LEFT, padx=10)
        
        self.button_clear = ttk.Button(root, text="Clear", command=self.clear_canvas)
        self.button_clear.pack(side=tk.RIGHT, padx=10)
        
        self.image = Image.new("L", (280, 280), color=255)
        self.draw = ImageDraw.Draw(self.image)
        
        # Bind the paint function to mouse movement
        self.canvas.bind("<B1-Motion>", self.paint)
        
    def paint(self, event):
        x1, y1 = (event.x - 5), (event.y - 5)
        x2, y2 = (event.x + 5), (event.y + 5)
        self.canvas.create_oval(x1, y1, x2, y2, fill='black', width=10)
        self.draw.ellipse([x1, y1, x2, y2], fill='black')
        
    def clear_canvas(self):
        self.canvas.delete("all")
        self.draw.rectangle([0, 0, 280, 280], fill='white')
        
    def save_and_predict(self):
        img = self.image.resize((28, 28))
        
        # Invert colors to match MNIST 
        inverted_img = ImageOps.invert(img)
        inverted_img.save("image_trial.png")
        print("Image saved as image_trial.png")
        
        self.predict_digit(inverted_img)
        
    def predict_digit(self, img):
        image_array = np.array(img) / 255.0  # Normalize
        image_array = image_array.reshape(1, 28*28)  # Flatten
        
        prediction = self.model.predict(image_array)
        predicted_label = np.argmax(prediction)
        
        print(f"Predicted Label: {predicted_label}")
        
        plt.imshow(img, cmap='gray')
        plt.title(f"Predicted Label: {predicted_label}")
        plt.show()

if __name__ == "__main__":
    model = load_model("mnist_model.h5")  
    
    root = tk.Tk()
    app = DrawingApp(root, model)
    root.mainloop()
