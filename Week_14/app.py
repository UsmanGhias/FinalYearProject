from flask import Flask, request, send_file, render_template
import os
import numpy as np
from pyrsgis import raster, convert
import tensorflow as tf
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'outputs'
MODEL_PATH = './SGDNet.h5'
model = tf.keras.models.load_model(MODEL_PATH)

@app.route('/', methods=['GET'])
def upload_form():
    return '''
    <!doctype html>
    <title>Upload an Image</title>
    <h1>Upload an Image for Prediction</h1>
    <form method=post enctype=multipart/form-data action="/upload">
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file and file.filename:
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Assuming file is a compatible raster
        predicted_output_path = predict(file_path)
        return send_file(predicted_output_path, as_attachment=True)
    return 'File not uploaded or incorrect file type.'

def predict(image_path):
    ds, image_data = raster.read(image_path, bands='all')
    image_data = convert.array_to_table(image_data)
    scaler = StandardScaler()
    image_data = scaler.fit_transform(image_data)
    image_data = image_data.reshape((image_data.shape[0], 1, image_data.shape[1]))
    predicted = model.predict(image_data)
    predicted_prob = predicted[:, 1]
    predicted_prob = np.reshape(predicted_prob, (ds.RasterYSize, ds.RasterXSize))

    output_path = os.path.join(app.config['OUTPUT_FOLDER'], 'predicted.tif')
    raster.export(predicted_prob, ds, filename=output_path, dtype='float')
    return output_path

if __name__ == '__main__':
    app.run(debug=True)

