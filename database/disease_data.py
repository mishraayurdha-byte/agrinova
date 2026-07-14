"""
==========================================================

AgriNova AI v2.0

PlantVillage Disease Knowledge Base

Part 1

==========================================================
"""

DISEASE_DATABASE = {

    # =====================================================
    # APPLE
    # =====================================================

    "Apple___Apple_scab": {

        "crop": "Apple",

        "severity": "Medium",

        "symptoms": [
            "Olive green spots on leaves",
            "Dark scabby lesions on fruits",
            "Premature leaf drop"
        ],

        "treatment":
        "Apply recommended fungicide and remove infected leaves.",

        "prevention":
        "Maintain orchard sanitation and use resistant varieties."

    },


    "Apple___Black_rot": {

        "crop": "Apple",

        "severity": "High",

        "symptoms": [
            "Brown leaf spots",
            "Black fruit rot",
            "Cankers on branches"
        ],

        "treatment":
        "Prune infected branches and spray fungicide.",

        "prevention":
        "Remove infected fruits and improve air circulation."

    },


    "Apple___Cedar_apple_rust": {

        "crop": "Apple",

        "severity": "Medium",

        "symptoms": [
            "Bright yellow leaf spots",
            "Orange fungal growth",
            "Leaf deformation"
        ],

        "treatment":
        "Apply rust-specific fungicide.",

        "prevention":
        "Remove nearby cedar hosts if possible."

    },


    "Apple___healthy": {

        "crop": "Apple",

        "severity": "Healthy",

        "symptoms": [
            "Healthy foliage",
            "No disease detected"
        ],

        "treatment":
        "No treatment required.",

        "prevention":
        "Continue regular monitoring."

    },


    # =====================================================
    # BLUEBERRY
    # =====================================================

    "Blueberry___healthy": {

        "crop": "Blueberry",

        "severity": "Healthy",

        "symptoms": [
            "Healthy leaves",
            "No visible infection"
        ],

        "treatment":
        "No treatment required.",

        "prevention":
        "Maintain irrigation and balanced nutrition."

    },


    # =====================================================
    # CHERRY
    # =====================================================

    "Cherry___Powdery_mildew": {

        "crop": "Cherry",

        "severity": "Medium",

        "symptoms": [
            "White powder on leaves",
            "Leaf curling",
            "Reduced growth"
        ],

        "treatment":
        "Apply sulfur-based fungicide.",

        "prevention":
        "Avoid excessive humidity."

    },


    "Cherry___healthy": {

        "crop": "Cherry",

        "severity": "Healthy",

        "symptoms": [
            "Healthy leaves",
            "No disease symptoms"
        ],

        "treatment":
        "No treatment required.",

        "prevention":
        "Regular orchard inspection."

    },


    # =====================================================
    # CORN
    # =====================================================

    "Corn___Cercospora_leaf_spot": {

        "crop": "Corn",

        "severity": "Medium",

        "symptoms": [
            "Rectangular gray lesions",
            "Leaf drying"
        ],

        "treatment":
        "Use appropriate fungicide.",

        "prevention":
        "Rotate crops and remove crop residue."

    },


    "Corn___Common_rust": {

        "crop": "Corn",

        "severity": "Medium",

        "symptoms": [
            "Rust-colored pustules",
            "Leaf yellowing"
        ],

        "treatment":
        "Spray fungicide if severe.",

        "prevention":
        "Grow resistant hybrids."

    },


    "Corn___Northern_Leaf_Blight": {

        "crop": "Corn",

        "severity": "High",

        "symptoms": [
            "Long gray-green lesions",
            "Rapid leaf drying"
        ],

        "treatment":
        "Apply systemic fungicide.",

        "prevention":
        "Crop rotation and resistant varieties."

    },


    "Corn___healthy": {

        "crop": "Corn",

        "severity": "Healthy",

        "symptoms": [
            "Healthy leaves",
            "No infection"
        ],

        "treatment":
        "No treatment required.",

        "prevention":
        "Maintain proper crop management."

    },
        # =====================================================
    # GRAPE
    # =====================================================

    "Grape___Black_rot": {

        "crop": "Grape",

        "severity": "High",

        "symptoms": [
            "Brown circular leaf spots",
            "Black shriveled berries",
            "Dark lesions on shoots"
        ],

        "treatment":
        "Apply fungicide and remove infected plant parts.",

        "prevention":
        "Ensure good air circulation and prune regularly."

    },


    "Grape___Esca": {

        "crop": "Grape",

        "severity": "High",

        "symptoms": [
            "Tiger stripe leaves",
            "Wood decay",
            "Sudden vine collapse"
        ],

        "treatment":
        "Remove infected vines and disinfect pruning tools.",

        "prevention":
        "Avoid trunk injuries and maintain vineyard hygiene."

    },


    "Grape___Leaf_blight": {

        "crop": "Grape",

        "severity": "Medium",

        "symptoms": [
            "Brown irregular leaf spots",
            "Leaf drying",
            "Premature defoliation"
        ],

        "treatment":
        "Apply copper fungicide.",

        "prevention":
        "Avoid overhead irrigation."

    },


    "Grape___healthy": {

        "crop": "Grape",

        "severity": "Healthy",

        "symptoms": [
            "Healthy green foliage",
            "No disease detected"
        ],

        "treatment":
        "No treatment required.",

        "prevention":
        "Continue regular vineyard management."

    },


    # =====================================================
    # ORANGE
    # =====================================================

    "Orange___Haunglongbing": {

        "crop": "Orange",

        "severity": "Very High",

        "symptoms": [
            "Yellow shoots",
            "Blotchy mottled leaves",
            "Small bitter fruits"
        ],

        "treatment":
        "Remove infected trees and control psyllid vectors.",

        "prevention":
        "Use certified disease-free planting material."

    },


    # =====================================================
    # PEACH
    # =====================================================

    "Peach___Bacterial_spot": {

        "crop": "Peach",

        "severity": "Medium",

        "symptoms": [
            "Small dark leaf spots",
            "Fruit lesions",
            "Leaf drop"
        ],

        "treatment":
        "Apply copper-based bactericide.",

        "prevention":
        "Avoid excessive moisture and prune regularly."

    },


    "Peach___healthy": {

        "crop": "Peach",

        "severity": "Healthy",

        "symptoms": [
            "Healthy leaves",
            "Healthy fruit"
        ],

        "treatment":
        "No treatment required.",

        "prevention":
        "Maintain proper orchard care."

    },


    # =====================================================
    # PEPPER
    # =====================================================

    "Pepper___Bacterial_spot": {

        "crop": "Pepper",

        "severity": "High",

        "symptoms": [
            "Dark leaf spots",
            "Fruit lesions",
            "Leaf yellowing"
        ],

        "treatment":
        "Use copper bactericide and remove infected plants.",

        "prevention":
        "Rotate crops and use certified seeds."

    },


    "Pepper___healthy": {

        "crop": "Pepper",

        "severity": "Healthy",

        "symptoms": [
            "Healthy foliage",
            "No infection detected"
        ],

        "treatment":
        "No treatment required.",

        "prevention":
        "Maintain balanced fertilization."

    },
        # =====================================================
    # POTATO
    # =====================================================

    "Potato___Early_blight": {

        "crop": "Potato",

        "severity": "High",

        "symptoms": [
            "Brown concentric rings",
            "Yellowing leaves",
            "Premature defoliation"
        ],

        "treatment":
        "Apply chlorothalonil or mancozeb fungicide.",

        "prevention":
        "Rotate crops and avoid overhead irrigation."

    },


    "Potato___Late_blight": {

        "crop": "Potato",

        "severity": "Very High",

        "symptoms": [
            "Water-soaked dark lesions",
            "White fungal growth",
            "Rapid plant collapse"
        ],

        "treatment":
        "Apply metalaxyl-based fungicide immediately.",

        "prevention":
        "Use certified seed potatoes and destroy infected plants."

    },


    "Potato___healthy": {

        "crop": "Potato",

        "severity": "Healthy",

        "symptoms": [
            "Healthy green leaves",
            "No disease symptoms"
        ],

        "treatment":
        "No treatment required.",

        "prevention":
        "Continue routine crop management."

    },


    # =====================================================
    # STRAWBERRY
    # =====================================================

    "Strawberry___Leaf_scorch": {

        "crop": "Strawberry",

        "severity": "Medium",

        "symptoms": [
            "Purple leaf spots",
            "Leaf edge scorching",
            "Reduced fruit yield"
        ],

        "treatment":
        "Apply appropriate fungicide and remove infected leaves.",

        "prevention":
        "Improve air circulation and avoid wet foliage."

    },


    "Strawberry___healthy": {

        "crop": "Strawberry",

        "severity": "Healthy",

        "symptoms": [
            "Healthy leaves",
            "Healthy fruit production"
        ],

        "treatment":
        "No treatment required.",

        "prevention":
        "Maintain proper irrigation and fertilization."

    },
        # =====================================================
    # TOMATO
    # =====================================================

    "Tomato___Bacterial_spot": {

        "crop": "Tomato",

        "severity": "High",

        "symptoms": [
            "Small dark leaf spots",
            "Yellow halos",
            "Fruit lesions"
        ],

        "treatment":
        "Apply copper-based bactericide.",

        "prevention":
        "Use certified seed and avoid overhead irrigation."

    },


    "Tomato___Early_blight": {

        "crop": "Tomato",

        "severity": "High",

        "symptoms": [
            "Brown concentric spots",
            "Lower leaf yellowing",
            "Leaf drop"
        ],

        "treatment":
        "Apply chlorothalonil or mancozeb fungicide.",

        "prevention":
        "Rotate crops and remove infected leaves."

    },


    "Tomato___Late_blight": {

        "crop": "Tomato",

        "severity": "Very High",

        "symptoms": [
            "Water-soaked lesions",
            "White fungal growth",
            "Rapid plant death"
        ],

        "treatment":
        "Spray metalaxyl or copper fungicide immediately.",

        "prevention":
        "Avoid excessive moisture and destroy infected plants."

    },


    "Tomato___Leaf_Mold": {

        "crop": "Tomato",

        "severity": "Medium",

        "symptoms": [
            "Yellow leaf patches",
            "Olive mold under leaves",
            "Leaf curling"
        ],

        "treatment":
        "Apply fungicide and improve greenhouse ventilation.",

        "prevention":
        "Reduce humidity and avoid overcrowding."

    },


    "Tomato___Septoria_leaf_spot": {

        "crop": "Tomato",

        "severity": "Medium",

        "symptoms": [
            "Small circular spots",
            "Gray leaf centers",
            "Leaf yellowing"
        ],

        "treatment":
        "Apply fungicide and remove infected foliage.",

        "prevention":
        "Rotate crops and keep foliage dry."

    },


    "Tomato___Spider_mites": {

        "crop": "Tomato",

        "severity": "Medium",

        "symptoms": [
            "Tiny yellow speckles",
            "Fine webbing",
            "Leaf bronzing"
        ],

        "treatment":
        "Apply miticide or neem oil.",

        "prevention":
        "Maintain proper irrigation and monitor regularly."

    },


    "Tomato___Target_Spot": {

        "crop": "Tomato",

        "severity": "High",

        "symptoms": [
            "Circular brown lesions",
            "Yellow margins",
            "Leaf drop"
        ],

        "treatment":
        "Apply systemic fungicide.",

        "prevention":
        "Avoid leaf wetness and rotate crops."

    },


    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {

        "crop": "Tomato",

        "severity": "Very High",

        "symptoms": [
            "Leaf curling",
            "Yellow leaves",
            "Stunted growth"
        ],

        "treatment":
        "Remove infected plants and control whiteflies.",

        "prevention":
        "Use virus-resistant varieties."

    },


    "Tomato___Tomato_mosaic_virus": {

        "crop": "Tomato",

        "severity": "High",

        "symptoms": [
            "Mosaic leaf pattern",
            "Leaf distortion",
            "Poor fruit quality"
        ],

        "treatment":
        "Remove infected plants and disinfect tools.",

        "prevention":
        "Avoid tobacco contamination and use clean seeds."

    },


    "Tomato___healthy": {

        "crop": "Tomato",

        "severity": "Healthy",

        "symptoms": [
            "Healthy green leaves",
            "Healthy fruits"
        ],

        "treatment":
        "No treatment required.",

        "prevention":
        "Maintain proper irrigation, nutrition and monitoring."

    }

}