import librosa
import numpy as np
import joblib

model = joblib.load("emotion_model.pkl")

def extract_features(file):
    audio, sr = librosa.load(file, sr=22050)
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)
    return np.mean(mfcc.T, axis=0).reshape(1, -1)

def predict_emotion(file):
    features = extract_features(file)
    prediction = model.predict(features)[0]
    return prediction
