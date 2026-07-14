"""
Image utility functions for AgriNova AI
"""

import cv2
import numpy as np


def preprocess_image(image_path, size=(224, 224)):
    """
    Read and preprocess an image for AI models.
    """

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(f"Unable to read image: {image_path}")

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, size)
    image = image.astype("float32") / 255.0
    image = np.expand_dims(image, axis=0)

    return image