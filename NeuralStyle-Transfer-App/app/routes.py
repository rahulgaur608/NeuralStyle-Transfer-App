from flask import Blueprint, render_template, request, jsonify, send_file
import os
from werkzeug.utils import secure_filename
from models.neural_style_transfer import StyleTransfer
from utils.image_processing import preprocess_image, save_image
import torch

main = Blueprint('main', __name__)

# Initialize the StyleTransfer model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
style_transfer = StyleTransfer(device)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/transfer-style', methods=['POST'])
def transfer_style():
    if 'content_image' not in request.files or 'style_image' not in request.files:
        return jsonify({'error': 'Both content and style images are required'}), 400
    
    content_image = request.files['content_image']
    style_image = request.files['style_image']
    
    if not (content_image and allowed_file(content_image.filename) and 
            style_image and allowed_file(style_image.filename)):
        return jsonify({'error': 'Invalid file format'}), 400
    
    try:
        # Process parameters
        style_weight = float(request.form.get('style_weight', 1e6))
        content_weight = float(request.form.get('content_weight', 1))
        num_steps = int(request.form.get('num_steps', 300))
        
        # Save and preprocess images
        content_path = os.path.join(current_app.config['UPLOAD_FOLDER'], 
                                  secure_filename(content_image.filename))
        style_path = os.path.join(current_app.config['UPLOAD_FOLDER'], 
                                secure_filename(style_image.filename))
        
        content_image.save(content_path)
        style_image.save(style_path)
        
        # Perform style transfer
        content_tensor = preprocess_image(content_path, device)
        style_tensor = preprocess_image(style_path, device)
        
        output_tensor = style_transfer.transfer_style(
            content_tensor, 
            style_tensor,
            num_steps=num_steps,
            style_weight=style_weight,
            content_weight=content_weight
        )
        
        # Save result
        result_filename = f"result_{os.path.splitext(content_image.filename)[0]}.png"
        result_path = os.path.join(current_app.config['RESULTS_FOLDER'], result_filename)
        save_image(output_tensor, result_path)
        
        return jsonify({
            'success': True,
            'result_url': f'/static/results/{result_filename}'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main.route('/examples')
def get_examples():
    examples_dir = os.path.join(current_app.static_folder, 'examples')
    examples = []
    
    for filename in os.listdir(examples_dir):
        if allowed_file(filename):
            examples.append({
                'url': f'/static/examples/{filename}',
                'name': os.path.splitext(filename)[0]
            })
    
    return jsonify(examples)

if __name__ == '__main__':
    from app import create_app
    app = create_app()
    app.run(debug=True) 