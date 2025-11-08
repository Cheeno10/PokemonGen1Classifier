import tensorflow as tf
import numpy as np
import sys
from PIL import Image

# --- 1. DEFINE CONSTANTS ---
# This line is now fixed to match your file name
MODEL_PATH = 'pokedex_model.keras' 
NAMES_PATH = 'pokemon_class_names.npy'
IMG_SIZE = 180 # Must be the same as your training!

# --- 2. LOAD THE MODEL AND CLASS NAMES ---
try:
    model = tf.keras.models.load_model(MODEL_PATH)
    class_names = np.load(NAMES_PATH, allow_pickle=True)
    print("✅ Model and class names loaded.")
except Exception as e:
    print(f"Error loading files: {e}")
    print(f"Make sure '{MODEL_PATH}' and '{NAMES_PATH}' are in the same folder.")
    sys.exit()

# --- 3. GET THE IMAGE PATH FROM THE TERMINAL ---
if len(sys.argv) < 2:
    print("Error: You must provide an image path.")
    print("Usage: python predict.py <path_to_your_image>")
    sys.exit()

image_path = sys.argv[1]

# --- 4. PRE-PROCESS THE IMAGE ---
try:
    # Open and resize the image
    img = Image.open(image_path).convert('RGB')
    img = img.resize((IMG_SIZE, IMG_SIZE))
    
    # Convert image to numpy array
    img_array = tf.keras.utils.img_to_array(img)
    
    # --- This is your 'normalization' step ---
    img_array = img_array / 255.0
    # ----------------------------------------
    
    # Create a batch
    img_array = tf.expand_dims(img_array, 0)
    
    print(f"Processing {image_path}...")

except Exception as e:
    print(f"Error processing image: {e}")
    sys.exit()


# --- 5. MAKE THE PREDICTION ---
predictions = model.predict(img_array)
score = predictions[0]

# --- 6. SHOW THE RESULT ---
predicted_pokemon = class_names[np.argmax(score)]
confidence = 100 * np.max(score)

print(f"\nThis image is most likely a {predicted_pokemon} with {confidence:.2f}% confidence.")