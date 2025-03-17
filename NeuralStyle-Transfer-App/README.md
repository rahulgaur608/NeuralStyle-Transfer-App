# Neural Style Transfer App 🎨 

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0.1-red.svg)](https://pytorch.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0.1-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Author](https://img.shields.io/badge/Author-Rahul%20Gaur-blue.svg)](https://portfolio-omega-nine-41.vercel.app/)

<div align="center">
  <img src="https://raw.githubusercontent.com/rahulgaur608/NeuralStyle-Transfer-App/main/static/images/banner.png" alt="Neural Style Transfer Banner" width="800"/>
</div>

## 🌟 Overview

Transform your photos into stunning artworks using the power of AI! This web application implements the Neural Style Transfer algorithm to apply artistic styles to your images. Built with PyTorch and Flask, it offers an intuitive interface for creating unique artistic compositions.

### 🎯 Key Features

- 🖼️ Upload content and style images through an intuitive web interface
- ⚡ Real-time style transfer processing with PyTorch
- 🎨 Multiple pre-loaded artistic styles to choose from
- 🎛️ Adjustable style transfer parameters
- 📱 Mobile-responsive design
- 🖥️ Modern, user-friendly interface
- 💾 Download and save your creations

## 🛠️ Technology Stack

<div align="center">
  <table>
    <tr>
      <td align="center"><b>Backend</b></td>
      <td align="center"><b>Frontend</b></td>
      <td align="center"><b>AI/ML</b></td>
      <td align="center"><b>DevOps</b></td>
    </tr>
    <tr>
      <td>
        • Python 3.8+<br/>
        • Flask<br/>
        • Werkzeug<br/>
        • Flask-CORS
      </td>
      <td>
        • HTML5<br/>
        • CSS3<br/>
        • JavaScript<br/>
        • Bootstrap 5
      </td>
      <td>
        • PyTorch<br/>
        • torchvision<br/>
        • PIL<br/>
        • OpenCV
      </td>
      <td>
        • Docker<br/>
        • Git<br/>
        • GitHub Actions<br/>
        • Gunicorn
      </td>
    </tr>
  </table>
</div>

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/rahulgaur608/NeuralStyle-Transfer-App.git
cd NeuralStyle-Transfer-App
```

2. Create and activate a virtual environment:
```bash
# On macOS/Linux
python -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app/routes.py
```

5. Open your browser and navigate to:
```
http://localhost:5000
```

## 💻 Usage Guide

1. **Upload Content Image**
   - Click "Choose File" or drag & drop your photo
   - This is the base image that will be transformed

2. **Select Style Image**
   - Choose from our gallery or upload your own
   - This image provides the artistic style

3. **Adjust Parameters (Optional)**
   - Style Weight: Controls style intensity (1e5 - 1e7)
   - Content Weight: Balances content preservation
   - Number of Steps: Affects quality and processing time

4. **Generate Artwork**
   - Click "Generate" and wait for processing
   - Download your stylized image when ready

## 🎨 Example Results

<div align="center">
  <table>
    <tr>
      <td align="center"><b>Content Image</b></td>
      <td align="center"><b>Style Image</b></td>
      <td align="center"><b>Result</b></td>
    </tr>
    <tr>
      <td><img src="static/examples/content1.jpg" width="200"/></td>
      <td><img src="static/examples/style1.jpg" width="200"/></td>
      <td><img src="static/examples/result1.jpg" width="200"/></td>
    </tr>
    <tr>
      <td><img src="static/examples/content2.jpg" width="200"/></td>
      <td><img src="static/examples/style2.jpg" width="200"/></td>
      <td><img src="static/examples/result2.jpg" width="200"/></td>
    </tr>
  </table>
</div>

## 🔧 Advanced Configuration

### Style Transfer Parameters

| Parameter | Description | Default | Range |
|-----------|-------------|---------|--------|
| `style_weight` | Controls style intensity | 1e6 | 1e5 - 1e7 |
| `content_weight` | Preserves content details | 1 | 0.1 - 10 |
| `num_steps` | Optimization iterations | 300 | 100 - 500 |
| `image_size` | Output resolution | 512 | 256 - 1024 |

### Environment Variables
Create a `.env` file in the root directory:
```env
FLASK_ENV=development
FLASK_APP=app/routes.py
MAX_CONTENT_LENGTH=16777216  # 16MB max file size
```

## 🐳 Docker Support

Build and run with Docker:
```bash
# Build the image
docker build -t neural-style-transfer .

# Run the container
docker run -p 5000:5000 neural-style-transfer
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/NewFeature`
3. Commit changes: `git commit -am 'Add NewFeature'`
4. Push to branch: `git push origin feature/NewFeature`
5. Submit a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Rahul Gaur**
- Portfolio: [portfolio-omega-nine-41.vercel.app](https://portfolio-omega-nine-41.vercel.app/)
- LinkedIn: [Rahul Gaur](https://www.linkedin.com/in/rahul-gaur-9570812a3/)
- GitHub: [@rahulgaur608](https://github.com/rahulgaur608)
- Email: rahulgaur608@gmail.com

## 🙏 Acknowledgments

- Neural Style Transfer algorithm based on [A Neural Algorithm of Artistic Style](https://arxiv.org/abs/1508.06576)
- Pre-trained VGG19 model provided by PyTorch
- Style images from various public domain art collections

## 📊 Development Roadmap & Contributions

### Upcoming Features
- [ ] Advanced style transfer algorithms implementation
- [ ] Real-time video style transfer
- [ ] Custom layer selection for style transfer
- [ ] Batch processing capabilities
- [ ] Style mixing and interpolation
- [ ] API endpoint documentation
- [ ] Performance optimizations

### How to Contribute Meaningfully
1. **Choose a Task**
   - Pick an open issue or propose a new feature
   - Comment on the issue to express your interest

2. **Development Guidelines**
   - Write clean, documented code
   - Follow PEP 8 style guidelines
   - Add unit tests for new features
   - Update documentation as needed

3. **Commit Best Practices**
   - Write clear, descriptive commit messages
   - Keep commits focused and atomic
   - Reference issues in commits when applicable
   - Regular, meaningful commits are better than sporadic large ones

4. **Quality Assurance**
   - Run tests before submitting PR
   - Ensure code passes linting
   - Test on different platforms if possible
   - Document any new dependencies

5. **Review Process**
   - Submit detailed PR descriptions
   - Respond to review comments
   - Be open to feedback and iterations
   - Help review other PRs

## 🚀 Featured AI Projects

### 1. Neural Style Transfer App (Current)
- Real-time artistic style transfer using deep learning
- PyTorch implementation of VGG19-based style transfer
- Web interface for interactive style manipulation
- Custom parameter tuning for optimal results

### 2. Deep Learning Vision Suite
- Multi-model computer vision pipeline
- Object detection and segmentation
- Face recognition and emotion analysis
- Real-time video processing capabilities

### 3. NLP Sentiment Analyzer
- BERT-based sentiment analysis model
- Multi-language support
- Real-time text processing
- REST API integration

### 4. AI Image Enhancement
- Super-resolution using GANs
- Image denoising and restoration
- Color correction and enhancement
- Batch processing support

### 5. Machine Learning Pipeline Framework
- Automated model training workflows
- Hyperparameter optimization
- Model performance monitoring
- A/B testing infrastructure

## 🌟 Project Goals

1. **Technical Excellence**
   - Implement state-of-the-art ML algorithms
   - Maintain high code quality standards
   - Optimize for performance and scalability

2. **Community Value**
   - Create useful features for real-world applications
   - Provide learning resources for AI/ML enthusiasts
   - Foster an inclusive development community

3. **Innovation**
   - Explore new style transfer techniques
   - Implement creative feature combinations
   - Push the boundaries of web-based ML applications

---

<div align="center">
  <p>If you find this project useful, please consider giving it a ⭐!</p>
  <p>Made with ❤️ by Rahul Gaur</p>
</div> 