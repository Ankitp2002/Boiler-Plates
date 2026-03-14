torch torchvision gradio albumentations Pillow numpy pandas matplotlib tqdm scikit-learn opencv-python

1. mkdir medical_image_classifier && cd medical_image_classifier
2. pip install -r requirements.txt
3. python setup.py # Setup data structure
4. # Download real dataset: kaggle.com/paultimothymooney/chest-xray-pneumonia
5. python train.py # Train (~30min CPU, 5min GPU)
6. python app.py # http://127.0.0.1:7860
