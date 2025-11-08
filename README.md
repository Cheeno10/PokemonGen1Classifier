# 🧬 Pokédex: Gen 1 Image Classifier  
Identify any of the original **151 Generation 1 Pokémon** from an image.

---

### 🚀 Overview
A machine learning model built using **TensorFlow/Keras** with **transfer learning (MobileNetV2)**.  
Training and fine-tuning were performed in **Google Colab**.

---

### 📂 Files in this Repository

| File | Description |
|------|-------------|
| `PokemonGen1Classifier.ipynb` | Google Colab notebook (dataset loading, training, and tuning). |
| `predict.py` | Script for running predictions locally. |
| `pokedex_model.keras` | Final trained model. |
| `pokemon_class_names.npy` | NumPy array mapping model outputs to Pokémon names. |

---

## 🖥️ How to Run (Local Prediction)

1. **Clone / Download** this repository.
2. Make sure these files are in the same folder:
   - `predict.py`
   - `pokedex_model.keras`
   - `pokemon_class_names.npy`

---

### ✅ Install Requirements

```bash
pip install tensorflow numpy pillow
```

---

### 🔍 Run a Prediction

> Example image: `mrmime.png` (must be in the same folder)

```bash
python predict.py mrmime.png
```

Expected output:

```
Model and class names loaded.
Processing mrmime.png...
This image is most likely a Mr. Mime with 99.78% confidence.
```

---

### 📦 Dataset Used
Model trained on the **“First Gen Pokémon Classification”** dataset (Kaggle).

---

⭐ If you find this useful, consider giving the project a star!
