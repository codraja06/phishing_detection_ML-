import os
import io
import json
import base64
import numpy as np
import tensorflow as tf
from PIL import Image
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# --- LOCAL METADATA ---
DISEASE_METADATA = {
    "Bacterial Spot": {
        "product": "Copper-based fungicides",
        "treatment": "Remove infected leaves immediately. Spray copper fungicide every 7-10 days. Avoid watering the leaves and water only at the base of the plant.",
        "product_url": "https://www.amazon.com/s?k=Copper+fungicide+for+tomatoes"
    },

    "Early Blight": {
        "product": "Chlorothalonil or Mancozeb",
        "treatment": "Remove affected leaves and dispose of them away from the garden. Spray fungicide every week. Keep mulch around the plant to prevent disease spread from soil.",
        "product_url": "https://www.amazon.com/s?k=Chlorothalonil+fungicide"
    },

    "Late Blight": {
        "product": "Ridomil Gold or Copper Fungicide",
        "treatment": "Remove heavily infected plants immediately to stop the spread. Spray recommended fungicide and avoid overhead watering. Ensure good airflow between plants.",
        "product_url": "https://www.amazon.com/s?k=Ridomil+Gold+fungicide"
    },

    "Leaf Mold": {
        "product": "Calcium-based sprays",
        "treatment": "Remove infected leaves and improve ventilation around plants. Reduce humidity and spray calcium-based products as recommended.",
        "product_url": "https://www.amazon.com/s?k=Calcium+spray+for+plants"
    },

    "Septoria Leaf Spot": {
        "product": "Fungicides containing chlorothalonil",
        "treatment": "Remove infected lower leaves. Apply fungicide every 7-10 days and avoid wetting the foliage while watering.",
        "product_url": "https://www.amazon.com/s?k=Septoria+fungicide"
    },

    "Spider Mites (Two-spotted Spider Mite)": {
        "product": "Neem oil or Insecticidal soap",
        "treatment": "Spray neem oil or insecticidal soap on both sides of the leaves. Repeat every 5-7 days until mites are controlled.",
        "product_url": "https://www.amazon.com/s?k=Neem+oil+for+plants"
    },

    "Target Spot": {
        "product": "Azoxystrobin or Chlorothalonil",
        "treatment": "Remove infected leaves and apply fungicide according to label instructions. Maintain proper spacing between plants for airflow.",
        "product_url": "https://www.amazon.com/s?k=Azoxystrobin+fungicide"
    },

    "Yellow Leaf Curl Virus": {
        "product": "Imidacloprid (for whitefly control)",
        "treatment": "Remove severely infected plants. Control whiteflies using insecticide or yellow sticky traps to prevent further spread.",
        "product_url": "https://www.amazon.com/s?k=Imidacloprid+insecticide"
    },

    "Mosaic Virus": {
        "product": "No chemical cure",
        "treatment": "Remove infected plants immediately. Disinfect gardening tools and control aphids to prevent the virus from spreading to healthy plants.",
        "product_url": "https://www.amazon.com/s?k=Aphid+control+organic"
    },

    "Healthy": {
        "product": "General purpose organic fertilizer",
        "treatment": "Continue regular watering, provide sufficient sunlight, and apply organic fertilizer every 2-3 weeks to maintain healthy growth.",
        "product_url": "https://www.amazon.com/s?k=Organic+tomato+fertilizer"
    }
}

CLASS_NAMES = list(DISEASE_METADATA.keys())

# --- INITIALIZE APP ---
app = FastAPI(title="Tomato Leaf Disease Detector Backend")

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- MODEL LOADING ---
# Updated to densernet.h5 as per your request
MODEL_PATH = "densernet.h5"
model = None

@app.on_event("startup")
def load_model():
    global model
    if os.path.exists(MODEL_PATH):
        try:
            model = tf.keras.models.load_model(MODEL_PATH)
            print(f"Model {MODEL_PATH} loaded successfully.")
        except Exception as e:
            print(f"Error loading model: {e}")
    else:
        print(f"Warning: {MODEL_PATH} not found. Prediction will use mock data.")

# --- HELPERS ---
def preprocess_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes))
    img = img.convert("RGB")
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# --- ENDPOINTS ---
@app.get("/")
def read_root():
    return {"status": "Tomato Leaf Disease System is running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image.")

    try:
        data = await file.read()
        
        # Mock prediction if no model exists (fallback to internal dictionary logic)
        if model is None:
            # For demo purposes when .h5 is missing
            disease_name = "Healthy"
            confidence = 0.95
        else:
            processed_data = preprocess_image(data)
            predictions = model.predict(processed_data)
            index = np.argmax(predictions[0])
            disease_name = CLASS_NAMES[index] if index < len(CLASS_NAMES) else "Unknown"
            confidence = float(predictions[0][index])

        metadata = DISEASE_METADATA.get(disease_name, DISEASE_METADATA["Healthy"])

        return {
            "disease_name": disease_name,
            "confidence_score": confidence,
            "recommended_product": metadata["product"],
            "natural_treatment": metadata["treatment"],
            "product_url": metadata.get("product_url", "")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
