from flask import Flask, request, send_file, jsonify
import rembg
import numpy as np
from PIL import Image
from flask_cors import CORS
import io
import os

app = Flask(__name__)

# CORS setup with allowed origins, methods, and headers
CORS(app, resources={r"/*": {"origins": ["http://localhost:3001", "https://f0-the-project.vercel.app"]}}, 
     supports_credentials=True)

@app.route('/', methods=['POST'])
def process_image():
    if 'file' not in request.files:
        return 'No file part', 400
    
    file = request.files['file']

    if file.filename == '':
        return 'No selected file', 400

    if file:
        input_image = Image.open(file.stream)

        input_array = np.array(input_image)

        output_array = rembg.remove(input_array)
        output_image = Image.fromarray(output_array)

        output_image = output_image.convert('RGB')

        img_io = io.BytesIO()
        output_image.save(img_io, 'JPEG')
        img_io.seek(0)

        return send_file(img_io, mimetype='image/jpeg', as_attachment=True, download_name='output_image.jpg')

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
