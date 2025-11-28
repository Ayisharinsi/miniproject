from flask import Flask, render_template, request, url_for
from inference import predict_image
import os

app = Flask(__name__)

# Absolute path to uploads folder
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static/uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    image_url = None
    if request.method == 'POST':
        file = request.files['image']
        if file:
            # Save the file
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(save_path)
            
            # Predict
            result = predict_image(save_path)
            
            # Create relative URL for template
            image_url = url_for('static', filename=f'uploads/{file.filename}')
    
    return render_template('index.html', result=result, filename=image_url)

if __name__ == '__main__':
    app.run(debug=True)
