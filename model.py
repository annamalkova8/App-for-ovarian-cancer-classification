import flask
from flask import Flask, request, jsonify
import pickle
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input
import numpy as np


# Load the pipeline from the saved file
with open('/Users/Anna/Study/skillfactory/theory/business/production/final_project/app/my_new_pipeline.pkl', 'rb') as pkl_file:
    pipe = pickle.load(pkl_file)

# Initialize the Flask app
app = Flask(__name__)

@app.route('/')
def index():
    msg = "Test message. Server is running!"
    return msg

@app.route('/predict', methods=['POST'])
def predict():
    # Get the image file and 'd' from the POST request
    file = request.files['image']
    d = request.form['number of slices']

    # Save the file to a temporary folder
    input_path = '/Users/Anna/Study/skillfactory/theory/business/production/final_project/image/input/temp_image.png'
    file.save(input_path)
    output_folder='/Users/Anna/Study/skillfactory/theory/business/production/final project/image/output'
    processed_image_path = pipe.named_steps['FeatureEngineering'].transform(input_path, output_folder, d)
    
    img = image.load_img(processed_image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)
    
    # Make predictions using the loaded pipeline
    test_datagen = ImageDataGenerator(rescale=1./255.)
    processed_image = test_datagen.flow(
    x=img_array,
    batch_size=1,
    shuffle=False
    )

    predictions = pipe.named_steps['ResNet'].predict(processed_image)
    predicted_classes = []
    classes = ['HGSC', 'EC', 'CC', 'LGSC', 'MC']
    for prediction in predictions:
        predicted_class_index = np.argmax(prediction)
        predicted_class = classes[predicted_class_index]  
        predicted_classes.append(predicted_class) 
    # Return the prediction
    return jsonify({'prediction': predicted_classes})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

    
    
#curl -X POST -F "image=@/Users/Anna/Study/skillfactory/theory/business/production/final_project/image/41_thumbnail.png" -F "d=1" http://localhost:5001/predict