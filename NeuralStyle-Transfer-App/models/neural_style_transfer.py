import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import copy

class VGG19Features(nn.Module):
    def __init__(self):
        super(VGG19Features, self).__init__()
        # Load pretrained VGG19 model
        vgg = models.vgg19(pretrained=True).features
        
        # Layers for content and style features
        self.content_layers = ['conv_4']
        self.style_layers = ['conv_1', 'conv_2', 'conv_3', 'conv_4', 'conv_5']
        
        # Create sequential modules for each layer
        self.layers = nn.ModuleList()
        self.layer_map = {}
        
        i = 0
        conv_count = 0
        for layer in vgg.children():
            if isinstance(layer, nn.Conv2d):
                conv_count += 1
                name = f'conv_{conv_count}'
            elif isinstance(layer, nn.ReLU):
                name = f'relu_{conv_count}'
                layer = nn.ReLU(inplace=False)
            elif isinstance(layer, nn.MaxPool2d):
                name = f'pool_{conv_count}'
            else:
                name = f'layer_{i}'
            
            self.layers.append(layer)
            self.layer_map[name] = i
            i += 1
    
    def forward(self, x):
        outputs = {}
        for i, layer in enumerate(self.layers):
            x = layer(x)
            # Store outputs for content and style layers
            for name, idx in self.layer_map.items():
                if i == idx:
                    if name in self.content_layers or name in self.style_layers:
                        outputs[name] = x
        return outputs

class StyleTransfer:
    def __init__(self, device):
        self.device = device
        self.vgg = VGG19Features().to(device).eval()
        # Freeze parameters
        for param in self.vgg.parameters():
            param.requires_grad = False
    
    def gram_matrix(self, tensor):
        """Calculate Gram Matrix for style loss"""
        b, c, h, w = tensor.size()
        features = tensor.view(b * c, h * w)
        gram = torch.mm(features, features.t())
        return gram.div(b * c * h * w)
    
    def get_features(self, image):
        """Extract features from image using VGG19"""
        return self.vgg(image)
    
    def content_loss(self, gen_features, content_features, layer):
        """Calculate content loss for a layer"""
        return F.mse_loss(gen_features[layer], content_features[layer])
    
    def style_loss(self, gen_features, style_features, layer):
        """Calculate style loss for a layer"""
        gen_gram = self.gram_matrix(gen_features[layer])
        style_gram = self.gram_matrix(style_features[layer])
        return F.mse_loss(gen_gram, style_gram)
    
    def transfer_style(self, content_img, style_img, num_steps=300,
                      style_weight=1e6, content_weight=1):
        """Perform neural style transfer"""
        # Initialize generated image with content image
        gen_img = content_img.clone().requires_grad_(True)
        optimizer = torch.optim.LBFGS([gen_img])
        
        content_features = self.get_features(content_img)
        style_features = self.get_features(style_img)
        
        # Training loop
        step = [0]
        while step[0] < num_steps:
            def closure():
                optimizer.zero_grad()
                gen_features = self.get_features(gen_img)
                
                # Content loss
                c_loss = sum(self.content_loss(gen_features, content_features, layer)
                            for layer in self.vgg.content_layers)
                
                # Style loss
                s_loss = sum(self.style_loss(gen_features, style_features, layer)
                            for layer in self.vgg.style_layers)
                
                # Total loss
                total_loss = content_weight * c_loss + style_weight * s_loss
                total_loss.backward()
                
                step[0] += 1
                return total_loss
            
            optimizer.step(closure)
        
        # Denormalize and clip
        gen_img = gen_img.clamp_(0, 1)
        return gen_img 