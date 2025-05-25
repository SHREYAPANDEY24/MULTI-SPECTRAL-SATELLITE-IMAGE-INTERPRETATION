from flask import Flask, request, jsonify, render_template
import numpy as np
import tensorflow as tf
from PIL import Image  

app = Flask(__name__)

# Load the trained CNN model
model = tf.keras.models.load_model("cnn_model.h5")  # Saves the model as cnn_model.h5
  
class_labels = ["cloudy", "desert", "green_area", "water"]  

# Home route to check if Flask is running
@app.route("/")
def home():
    return render_template("index.html")

# Image upload & prediction route
@app.route("/upload", methods=["POST"])
def upload_image():
    if "image" not in request.files:
        return jsonify({"error": "No file uploaded!"}), 400
    
    file = request.files["image"]  # Get uploaded image

    try:
        # 🖼️ Preprocess the image for the CNN model
        image = Image.open(file).resize((224, 224))  # Resize image  
        image_array = np.array(image) / 255.0  # Normalize  
        image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension  

        # 🤖 Get prediction from CNN model  
        prediction = model.predict(image_array)  
        predicted_class = np.argmax(prediction)
        predicted_label = class_labels[predicted_class]   # Get highest confidence class  

        return jsonify({"message": "Image processed successfully!", "predicted_class": int(predicted_class)})
    
    except Exception as e:
        return jsonify({"error": f"Failed to process image: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
