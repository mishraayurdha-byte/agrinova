"""
==========================================================
AgriNova AI v2.0
Image Processing Utility

Used for:
- Disease Detection
- Image Validation
- TensorFlow Preprocessing

==========================================================
"""

from pathlib import Path

import cv2
import numpy as np

from PIL import Image

from utils.constants import (
    MODEL_IMAGE_HEIGHT,
    MODEL_IMAGE_WIDTH,
    MODEL_CHANNELS
)


# ==========================================================
# Image Validation
# ==========================================================

def image_exists(image_path):
    """
    Check whether an image exists.
    """

    return Path(image_path).is_file()


# ==========================================================
# Load Image (PIL)
# ==========================================================

def load_image(image_path):
    """
    Load image using Pillow.
    """

    return Image.open(image_path).convert("RGB")


# ==========================================================
# Resize Image
# ==========================================================

def resize_image(image):
    """
    Resize image for AI model.
    """

    return image.resize(

        (

            MODEL_IMAGE_WIDTH,

            MODEL_IMAGE_HEIGHT

        )

    )


# ==========================================================
# Normalize Image
# ==========================================================

def normalize_image(image):
    """
    Normalize pixels between 0 and 1.
    """

    image = np.asarray(

        image,

        dtype=np.float32

    )

    image /= 255.0

    return image


# ==========================================================
# Convert to Tensor
# ==========================================================

def image_to_tensor(image):
    """
    Convert image to model tensor.

    Shape:
    (1,224,224,3)
    """

    return np.expand_dims(

        image,

        axis=0

    )


# ==========================================================
# Complete Preprocessing Pipeline
# ==========================================================

def preprocess_image(image_path):
    """
    Complete preprocessing pipeline.
    """

    if not image_exists(image_path):

        raise FileNotFoundError(

            f"Image not found: {image_path}"

        )

    image = load_image(image_path)

    image = resize_image(image)

    image = normalize_image(image)

    tensor = image_to_tensor(image)

    return tensor


# ==========================================================
# OpenCV Loader
# ==========================================================

def preprocess_cv_image(image_path):
    """
    Load image using OpenCV.
    """

    image = cv2.imread(image_path)

    if image is None:

        raise ValueError(

            "Unable to read image."

        )

    image = cv2.cvtColor(

        image,

        cv2.COLOR_BGR2RGB

    )

    image = cv2.resize(

        image,

        (

            MODEL_IMAGE_WIDTH,

            MODEL_IMAGE_HEIGHT

        )

    )

    image = image.astype(

        np.float32

    ) / 255.0

    image = np.reshape(

        image,

        (

            1,

            MODEL_IMAGE_HEIGHT,

            MODEL_IMAGE_WIDTH,

            MODEL_CHANNELS

        )

    )

    return image


# ==========================================================
# Prediction Helper
# ==========================================================

def prepare_prediction(image_path):
    """
    Prepare image for TensorFlow prediction.
    """

    return preprocess_image(image_path)