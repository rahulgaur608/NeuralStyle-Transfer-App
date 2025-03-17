document.addEventListener('DOMContentLoaded', function() {
    // Form elements
    const form = document.getElementById('styleTransferForm');
    const contentInput = document.getElementById('contentImage');
    const styleInput = document.getElementById('styleImage');
    const styleWeight = document.getElementById('styleWeight');
    const numSteps = document.getElementById('numSteps');
    const generateBtn = document.getElementById('generateBtn');
    const loadingSpinner = document.getElementById('loadingSpinner');
    const resultImage = document.getElementById('resultImage');
    const downloadBtn = document.getElementById('downloadBtn');
    
    // Preview elements
    const contentPreview = document.getElementById('contentPreview');
    const stylePreview = document.getElementById('stylePreview');
    
    // Range value displays
    const styleWeightValue = document.getElementById('styleWeightValue');
    const numStepsValue = document.getElementById('numStepsValue');
    
    // Update range value displays
    styleWeight.addEventListener('input', function() {
        styleWeightValue.textContent = this.value;
    });
    
    numSteps.addEventListener('input', function() {
        numStepsValue.textContent = this.value;
    });
    
    // Handle image uploads and previews
    function handleImageUpload(input, previewElement) {
        const file = input.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                const img = document.createElement('img');
                img.src = e.target.result;
                previewElement.innerHTML = '';
                previewElement.appendChild(img);
                previewElement.classList.add('fade-in');
            };
            reader.readAsDataURL(file);
        }
    }
    
    contentInput.addEventListener('change', function() {
        handleImageUpload(this, contentPreview);
    });
    
    styleInput.addEventListener('change', function() {
        handleImageUpload(this, stylePreview);
    });
    
    // Handle form submission
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Show loading state
        generateBtn.disabled = true;
        loadingSpinner.classList.remove('d-none');
        resultImage.innerHTML = '';
        downloadBtn.classList.add('d-none');
        
        // Create form data
        const formData = new FormData();
        formData.append('content_image', contentInput.files[0]);
        formData.append('style_image', styleInput.files[0]);
        formData.append('style_weight', Math.pow(10, styleWeight.value));
        formData.append('num_steps', numSteps.value);
        
        try {
            const response = await fetch('/transfer-style', {
                method: 'POST',
                body: formData
            });
            
            const data = await response.json();
            
            if (data.success) {
                // Display result
                const img = document.createElement('img');
                img.src = data.result_url;
                img.onload = function() {
                    resultImage.innerHTML = '';
                    resultImage.appendChild(img);
                    resultImage.classList.add('fade-in');
                    
                    // Show download button
                    downloadBtn.href = data.result_url;
                    downloadBtn.download = 'styled_image.png';
                    downloadBtn.classList.remove('d-none');
                };
            } else {
                throw new Error(data.error || 'Style transfer failed');
            }
        } catch (error) {
            // Show error message
            resultImage.innerHTML = `
                <div class="alert alert-danger">
                    <i class="fas fa-exclamation-circle"></i>
                    ${error.message}
                </div>
            `;
        } finally {
            // Reset loading state
            generateBtn.disabled = false;
            loadingSpinner.classList.add('d-none');
        }
    });
    
    // Load example images
    async function loadExamples() {
        try {
            const response = await fetch('/examples');
            const examples = await response.json();
            
            const container = document.getElementById('examplesContainer');
            examples.forEach(example => {
                const col = document.createElement('div');
                col.className = 'col-md-4 example-item';
                col.innerHTML = `
                    <img src="${example.url}" alt="${example.name}" class="img-fluid">
                    <p class="text-center mt-2">${example.name}</p>
                `;
                container.appendChild(col);
            });
        } catch (error) {
            console.error('Failed to load examples:', error);
        }
    }
    
    // Initialize examples
    loadExamples();
    
    // Add drag and drop support
    function setupDragAndDrop(dropZone, input) {
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            dropZone.addEventListener(eventName, preventDefaults, false);
        });
        
        function preventDefaults(e) {
            e.preventDefault();
            e.stopPropagation();
        }
        
        ['dragenter', 'dragover'].forEach(eventName => {
            dropZone.addEventListener(eventName, highlight, false);
        });
        
        ['dragleave', 'drop'].forEach(eventName => {
            dropZone.addEventListener(eventName, unhighlight, false);
        });
        
        function highlight(e) {
            dropZone.classList.add('border-primary');
        }
        
        function unhighlight(e) {
            dropZone.classList.remove('border-primary');
        }
        
        dropZone.addEventListener('drop', handleDrop, false);
        
        function handleDrop(e) {
            const dt = e.dataTransfer;
            const files = dt.files;
            
            input.files = files;
            handleImageUpload(input, dropZone);
        }
    }
    
    // Set up drag and drop for both upload zones
    setupDragAndDrop(contentPreview, contentInput);
    setupDragAndDrop(stylePreview, styleInput);
}); 