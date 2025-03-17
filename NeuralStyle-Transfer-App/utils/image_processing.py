import torch
import torchvision.transforms as transforms
from PIL import Image
import numpy as np

def load_image(image_path, max_size=None):
    """Load and preprocess an image"""
    image = Image.open(image_path)
    
    # Convert to RGB if necessary
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Resize if max_size is specified
    if max_size:
        if max(image.size) > max_size:
            size = max_size
            image = image.resize((size, size), Image.LANCZOS)
    
    return image

def preprocess_image(image_path, device, max_size=512):
    """Convert image to tensor and normalize"""
    image = load_image(image_path, max_size)
    
    # Define transforms
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                           std=[0.229, 0.224, 0.225])
    ])
    
    # Add batch dimension
    image = transform(image).unsqueeze(0)
    
    return image.to(device)

def deprocess_image(tensor):
    """Convert tensor back to image"""
    # Clone the tensor to avoid modifying it
    image = tensor.cpu().clone().detach()
    
    # Remove the batch dimension
    image = image.squeeze()
    
    # Unnormalize
    image = image * torch.tensor([0.229, 0.224, 0.225]).view(3, 1, 1)
    image = image + torch.tensor([0.485, 0.456, 0.406]).view(3, 1, 1)
    
    # Clip values to [0, 1]
    image = image.clamp(0, 1)
    
    # Convert to PIL Image
    transform = transforms.ToPILImage()
    image = transform(image)
    
    return image

def save_image(tensor, save_path):
    """Save tensor as image"""
    image = deprocess_image(tensor)
    image.save(save_path)

def create_gif(image_list, save_path, duration=500):
    """Create a GIF from a list of images"""
    images = [Image.open(img) for img in image_list]
    images[0].save(
        save_path,
        save_all=True,
        append_images=images[1:],
        duration=duration,
        loop=0
    )

def resize_with_aspect_ratio(image, max_size):
    """Resize image while maintaining aspect ratio"""
    aspect_ratio = min(max_size/float(image.size[0]), 
                      max_size/float(image.size[1]))
    new_size = tuple([int(x*aspect_ratio) for x in image.size])
    return image.resize(new_size, Image.LANCZOS)

def create_image_grid(images, rows, cols):
    """Create a grid of images"""
    w, h = images[0].size
    grid = Image.new('RGB', size=(cols*w, rows*h))
    
    for idx, image in enumerate(images):
        i = idx % cols
        j = idx // cols
        grid.paste(image, box=(i*w, j*h))
    
    return grid 