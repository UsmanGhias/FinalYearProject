from odoo import models, fields, api
import base64
import io
import numpy as np
from tensorflow.keras.models import load_model
import rasterio
from rasterio.io import MemoryFile
from sklearn.preprocessing import StandardScaler\


class GlacierImage(models.Model):
    _name = 'glacier.image'
    _description = 'Glacier Image Analysis'

    name = fields.Char('Description')
    image = fields.Binary('Image', attachment=True)
    prediction = fields.Char('Prediction')

    def preprocess_image(self, image_data):
        try:
            with MemoryFile(io.BytesIO(base64.b64decode(image_data))) as memfile:
                with memfile.open() as dataset:
                    # Assume the model needs a specific number of features
                    image_array = dataset.read()
                    image_flattened = image_array.flatten()
                    # Ensure we have exactly 9 features
                    if len(image_flattened) >= 9:
                        features = image_flattened[:9]  # Extract the first 9 features
                    else:
                        return "Insufficient data for prediction"
                    scaler = StandardScaler()
                    scaled_features = scaler.fit_transform(features.reshape(-1, 1))
                    return scaled_features.reshape(1, -1)
        except Exception as e:
            return str(e)  # Proper error handling

    def make_prediction(self):
        processed_image = self.preprocess_image(self.image)
        if isinstance(processed_image, str):
            self.prediction = processed_image  # Handling errors
            return
        model_path = '/home/usmanghias/UsmanGhias/Final_Year_Project/Deep_Learning/Script/SGDNet.h5'
        model = load_model(model_path)
        prediction = model.predict(processed_image)
        self.prediction = str(np.argmax(prediction, axis=1)[0])

    @api.model
    def create(self, vals):
        record = super(GlacierImage, self).create(vals)
        record.make_prediction()
        return record
