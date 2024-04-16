from flask import Flask, render_template, request
from deepface import DeepFace

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return render_template('index.html', message='No file part')
    
    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', message='No selected file')
    
    if file:
        # Save the uploaded file to a temporary location
        image_path = 'temp.jpg'
        file.save(image_path)
        
        # Perform emotion detection using DeepFace
        result = DeepFace.analyze(image_path,actions = [ 'emotion'])
        emotion = result
        
        return render_template('result.html', emotion=emotion)
    
    return render_template('index.html', message='Error')

if __name__ == '__main__':
    app.run(debug=True)
