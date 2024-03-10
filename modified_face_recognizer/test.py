import face_recognition
import cv2
import numpy as np
from pathlib import Path
import pickle

encodings_location = Path("./output/encodings.pkl")
with encodings_location.open(mode="rb") as f:
    loaded_encodings = pickle.load(f)

print(loaded_encodings)