# Pokédex: Gen 1 Image Classifier

A machine learning model that identifies any of the original **151 Generation 1 Pokémon** from an image.  
Built using **TensorFlow/Keras** with **MobileNetV2 transfer learning**. Training and fine-tuning were done in **Google Colab**.

---

## Repository Files

| File | Description |
|------|-------------|
| `PokemonGen1Classifier.ipynb` | Google Colab notebook containing data loading, model building, training, and tuning. |
| `predict.py` | Script used to run local predictions. |
| `pokedex_model.keras` | Final trained TensorFlow/Keras model. |
| `pokemon_class_names.npy` | NumPy array mapping model output to the corresponding Pokémon name. |

---

## How to Run (Local Prediction)

1. Clone or download the repository.
2. Ensure the following files are in the same folder:
   - `predict.py`
   - `pokedex_model.keras`
   - `pokemon_class_names.npy`

### Install requirements

```bash
pip install tensorflow numpy pillow
```

### Run a prediction

Place an image (example: `mrmime.png`) in the same folder, then run:

```bash
python predict.py mrmime.png
```

Example output:

```
Model and class names loaded.
Processing mrmime.png...
This image is most likely a Mr. Mime with 99.78% confidence.
```

---

## Dataset

Trained on the [**"First Gen Pokémon Classification"**](https://www.kaggle.com/datasets/rogerkoala/first-gen-pokemon) dataset (Kaggle).

