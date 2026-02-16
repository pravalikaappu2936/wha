import librosa
import numpy as np
import os
from sklearn.ensemble import RandomForestClassifier
import joblib

DATA_PATH = "dataset"

EMOTIONS = ["neutral", "happy", "sad", "angry", "fear", "stress"]

X = []
y = []

def extract_features(file_path):
    audio, sr = librosa.load(file_path, sr=22050)
    
    mfcc = librosa.feature.mfcc(
        y=audio,
        sr=sr,
        n_mfcc=40
    )
    
    mfcc_mean = np.mean(mfcc.T, axis=0)
    return mfcc_mean

print("📂 Loading dataset...")

for emotion in EMOTIONS:
    folder = os.path.join(DATA_PATH, emotion)
    
    for file in os.listdir(folder):
        if file.endswith(".wav"):
            file_path = os.path.join(folder, file)
            
            try:
                features = extract_features(file_path)
                X.append(features)
                y.append(emotion)
            except:
                print("Error processing:", file)

print("🤖 Training model...")
model = RandomForestClassifier(n_estimators=200)
model.fit(X, y)

joblib.dump(model, "emotion_model.pkl")

print("✅ emotion_model.pkl created successfully!")
