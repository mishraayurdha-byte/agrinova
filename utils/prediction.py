import tensorflow as tf
import numpy as np
import json
import os

from PIL import Image


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "disease_model.h5"
)


CLASS_PATH = os.path.join(
    BASE_DIR,
    "models",
    "class_names.json"
)


# Load model
model = tf.keras.models.load_model(
    MODEL_PATH
)


# Load class names
with open(CLASS_PATH, "r") as f:
    CLASS_NAMES = json.load(f)



def predict_disease(image_path):

    img = Image.open(image_path).convert("RGB")

    img = img.resize(
        (224,224)
    )


    img_array = np.array(
        img,
    dtype=np.float32
        )


    img_array = np.expand_dims(
        img_array,
        axis=0
    )


    img_array = img_array / 255.0


    prediction = model.predict(
        img_array,
        verbose=0
    )


    index = np.argmax(
        prediction
    )


    confidence = float(
        np.max(prediction)
    ) * 100
        


   
    index = int(index)
    if str(index) not in CLASS_NAMES:
        raise ValueError(
            f"Invalid class index {index}. "
            f"Available classes: {list(CLASS_NAMES.keys())}"
        )
    class_name = CLASS_NAMES[str(index)]

    
                


    if "___" in class_name:

        crop, disease = class_name.split(
            "___",
            1
        )

    else:

        crop = "Unknown"
        disease = class_name



    return {

        "crop": crop,

        "disease": disease.replace(
            "_",
            " "
        ).title(),

        "confidence": round(
            confidence,
            2
        )

    }