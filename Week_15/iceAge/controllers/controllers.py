from odoo import http
from odoo.http import request

class GlacierController(http.Controller):
    @http.route('/glacier/predict', type='http', auth="public", methods=['POST'], csrf=False)
    def upload_and_predict(self, **kw):
        if 'image_upload' in request.httprequest.files:
            image_file = request.httprequest.files['image_upload']
            image_data = base64.b64encode(image_file.read())
            # Create a new record
            glacier_image = request.env['glacier.image'].create({
                'name': 'Uploaded Image',
                'image': image_data,
            })
            # Redirect or respond with prediction
            return request.make_response('Prediction: %s' % glacier_image.prediction)
        return "No image uploaded"
