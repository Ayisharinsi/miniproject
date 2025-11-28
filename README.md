## FRESH FRUIT AND VEGETABLE SPOILAGE DETECTION SYSTEM
## About:
The Food Spoilage Detection project leverages computer vision and deep learning to automatically identify spoiled food items from images. Using a Vision Transformer (ViT) model, the system classifies images of fruits and vegetables as fresh or spoiled. This project provides a real-time, automated, and reliable method for monitoring food quality, reducing wastage, and enhancing food safety.

Built with Python and libraries like PyTorch, Torchvision, timm, and PIL, the system captures images via a web interface and predicts food freshness using a trained ViT model. It offers immediate feedback, making it suitable for households, grocery stores, and restaurants aiming to manage food efficiently and safely.

## Features:

Automated Food Spoilage Detection: Classifies food items as fresh or spoiled in real-time.

Deep Learning Model: Uses a Vision Transformer (ViT) trained on images of fruits and vegetables.

Web Interface: Users can upload images via a Flask-based web app.

Confidence-Based Alerts: Provides warnings if the model is uncertain about the classification.

Multi-Food Support: Works with various fruits and vegetables.

Real-Time Feedback: Instant prediction displayed on the interface for quick decision-making.

## Requirements:

Programming Language: Python 3.7+
Libraries:

PyTorch: For building and running deep learning models.

Torchvision: For dataset handling and image transforms.

timm: For pretrained Vision Transformer (ViT) model.

OpenCV / PIL: For image processing.

Flask: For building the web interface.

## Hardware:

Camera or image upload support via web.

Moderate CPU/GPU for real-time inference.

IDE: Any Python-compatible IDE (PyCharm, VS Code, Jupyter Notebook).

System Architecture:

Input Capture:

Users upload images of food items via the Flask web interface.

Preprocessing:

Images are resized to 224x224, normalized, and transformed into tensors.

Spoilage Prediction:

The pre-trained Vision Transformer (ViT) model predicts whether the food is fresh or spoiled.

Softmax probabilities are calculated to provide confidence scores.

## Result Display:

Flask renders the prediction and confidence percentage on the web page.

If the confidence is below 70%, a warning is displayed to indicate uncertainty.

Model Training (Optional):

Model can be retrained using additional labeled datasets for improved accuracy.

Trains with data augmentations (resize, horizontal flip, normalization) for robustness.

## Output:
<img width="1905" height="1079" alt="image" src="https://github.com/user-attachments/assets/8308fead-6ec3-437e-a1f5-e7dc50f0cbfa" />

<img width="1918" height="1079" alt="image" src="https://github.com/user-attachments/assets/a07686ad-6b9d-404f-8464-ce75537d4440" />

<img width="1907" height="1079" alt="image" src="https://github.com/user-attachments/assets/71b1e92b-1512-4993-9ed6-8a49329b786f" />


## Impact:

Food Safety: Prevents consumption of spoiled or unsafe food.

Food Waste Reduction: Helps households and stores manage inventory efficiently.

Automation: Reduces the need for manual inspection.

Innovation in AI Applications: Demonstrates practical use of ViT and deep learning in everyday life.


## Results:

Accurately classifies fruits and vegetables as fresh or spoiled in real-time.

Provides clear feedback to reduce human error in food inspection.

Robust to different lighting and angles in image uploads.

## Articles Published / References:
“Real-Time Food Spoilage Detection Using Deep Learning” – International Journal of Computer Applications, 2021.

“Automatic Food Freshness Monitoring Using Computer Vision” – IEEE Access, 2020.

“Machine Learning for Food Quality and Safety” – Journal of Food Engineering, 2019.
