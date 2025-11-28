# inference.py
import torch
from PIL import Image
from torchvision import transforms
from models import get_vit_model  # Make sure this matches your models.py

# -----------------------------
# 1. Load the model once
# -----------------------------
model = get_vit_model(num_classes=2)
state_dict = torch.load("vit_food.pth", map_location="cpu")
model.load_state_dict(state_dict)
model.eval()  # Set model to evaluation mode

classes = ['fresh', 'spoiled']  # Your class labels

# -----------------------------
# 2. Define a prediction function
# -----------------------------
def predict_image(image_path):
    # Load and transform image
    transform = transforms.Compose([
        transforms.Resize((224, 224)),  # ViT expects 224x224
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])
    image = Image.open(image_path).convert('RGB')
    image = transform(image).unsqueeze(0)  # Add batch dimension

    # Run inference
    with torch.no_grad():
        outputs = model(image)
        _, predicted = torch.max(outputs, 1)
    
    return classes[predicted.item()]
