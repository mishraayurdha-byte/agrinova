"""
==========================================================

AgriNova AI v2.0

Disease Prediction Service

EfficientNetB0 Inference

Supports:
- PlantVillage 38 Classes
- Top-3 Predictions
- Disease History
- Knowledge Base
- Confidence Score

==========================================================
"""

from pathlib import Path
import json
import os

import numpy as np
import tensorflow as tf

from PIL import Image

from database import db
from database.models import DiseaseHistory

from database.disease_data import DISEASE_DATABASE



# ==========================================================
# Configuration
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "disease_model.h5"

CLASS_PATH = BASE_DIR / "models" / "class_names.json"

IMAGE_SIZE = (224, 224)

CONFIDENCE_THRESHOLD = 50.0



# ==========================================================
# Disease Service
# ==========================================================

class DiseaseService:

    def __init__(self):

        print("\nLoading Disease Detection Model...")

        self.model = tf.keras.models.load_model(

            MODEL_PATH,

            compile=False

        )

        print("Model Loaded Successfully")



        with open(

            CLASS_PATH,

            "r",

            encoding="utf-8"

        ) as file:

            self.class_names = json.load(file)



        # Support both dict and list

        if isinstance(self.class_names, list):

            self.class_names = {

                str(i): name

                for i, name

                in enumerate(self.class_names)

            }



        print(

            f"{len(self.class_names)} Classes Loaded"

        )



    # ======================================================
    # Image Preprocessing
    # ======================================================

    def preprocess_image(

        self,

        image_path

    ):

        image = Image.open(

            image_path

        ).convert(

            "RGB"

        )



        image = image.resize(

            IMAGE_SIZE

        )



        image = np.array(

            image,

            dtype=np.float32

        )



        image = image / 255.0



        image = np.expand_dims(

            image,

            axis=0

        )



        return image
    
        # ======================================================
    # Prediction
    # ======================================================

    def predict(

        self,

        image_path

    ):

        try:

            image = self.preprocess_image(

                image_path

            )


            prediction = self.model.predict(

                image,

                verbose=0
                

            )[0]
            print("=" * 50)
            print("Disease prediction started")
            print("Image path:", image_path)

            image = self.preprocess_image(image_path)
            print("Preprocessing completed")
            print("Image shape:", image.shape)

            prediction = self.model.predict(image, verbose=0)[0]
            print("Prediction completed")

            predicted_index = np.argmax(prediction)
            print("Predicted Index:", predicted_index)
            print("Confidence:", prediction[predicted_index] * 100)


            predicted_index = int(

                np.argmax(

                    prediction

                )

            )


            confidence = float(

                prediction[predicted_index] * 100

            )


            # ===============================================
            # Top 3 Predictions
            # ===============================================

            top3_indexes = np.argsort(

                prediction

            )[-3:][::-1]


            top_predictions = []


            print("\n==============================")

            print("TOP 3 PREDICTIONS")

            print("==============================")


            for index in top3_indexes:


                class_name = self.class_names.get(

                    str(index),

                    "Unknown"

                )


                score = round(

                    float(prediction[index]) * 100,

                    2

                )


                print(

                    f"{index} -> {class_name} : {score}%"

                )


                if "___" in class_name:

                    crop_name, disease_name = class_name.split(

                        "___",

                        1

                    )

                else:

                    crop_name = "Unknown"

                    disease_name = class_name


                top_predictions.append(

                    {

                        "rank": len(top_predictions) + 1,

                        "crop": crop_name,

                        "disease": disease_name,

                        "confidence": score,

                        "class_name": class_name

                    }

                )


            predicted_class = top_predictions[0]["class_name"]


            crop = top_predictions[0]["crop"]


            disease = top_predictions[0]["disease"]


            print("\n==============================")

            print("Final Prediction")

            print("==============================")

            print("Crop      :", crop)

            print("Disease   :", disease)

            print("Confidence:", confidence)

            print("==============================")
        # ======================================================
        # Confidence Check
        # ======================================================

            if confidence < CONFIDENCE_THRESHOLD:

                return {

                    "success": False,

                    "message": "Low confidence prediction.",

                    "confidence": round(confidence, 2)

                }


        # ======================================================
        # Disease Knowledge Base
        # ======================================================

            disease_info = DISEASE_DATABASE.get(

                    predicted_class,

                    {

                        "severity": "Unknown",

                        "symptoms": [],

                        "treatment": "No treatment available.",

                        "prevention": "Consult an agricultural expert."

                    }

                )

        # ======================================================
        # Save Prediction History
        # ======================================================

            history = DiseaseHistory(

                    image_name=os.path.basename(

                        str(image_path)

                    ),

                     crop_name=crop,

                    disease_name=disease,

                    confidence=round(
                        confidence,
                        2
                    )

                )

            db.session.add(history)

            db.session.commit()


        # ======================================================
        # Final Response
        # ======================================================

            result = {

            "success": True,

            "crop": crop,

            "disease": disease,

            "class_name": predicted_class,

            "confidence": round(confidence, 2),

            "severity": disease_info["severity"],

            "symptoms": disease_info["symptoms"],

            "treatment": disease_info["treatment"],

            "prevention": disease_info["prevention"],

            "top_predictions": top_predictions

                    }

            return result

    # ======================================================
    # Exception Handling
    # ======================================================

        except Exception as e:
            import traceback
            traceback.print_exc()
                   
            

                    

            return {

                        "success": False,

                        "message": str(e)

                    }
       