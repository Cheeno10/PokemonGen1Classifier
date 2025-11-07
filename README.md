Pokédex: Gen 1 Image Classifier 🧬

A machine learning model that identifies any of the original 151 Generation 1 Pokémon from an image.
Built using TensorFlow/Keras with transfer learning based on the MobileNetV2 architecture.
Training and fine-tuning were done in Google Colab.

Files in This Repository:

PokemonGen1Classifier.ipynb — Google Colab notebook containing dataset loading, model building, training, and tuning.

predict.py — Python script used to run predictions locally.

pokedex_model.keras — The final trained TensorFlow/Keras model.

pokemon_class_names.npy — NumPy array that maps the model’s output to the correct Pokémon name.

How to Run (Local Prediction)

Clone or download this repository and ensure the following files are in the same folder:

predict.py

pokedex_model.keras

pokemon_class_names.npy

1. Install the required libraries:

pip install tensorflow numpy pillow


2. Run a prediction. Place a test image (example: mrmine.png) in the same folder, then run:

python predict.py mrmine.png


You should see something like:

✅ Model and class names loaded.
Processing mrmine.png...
This image is most likely a Mr. Mime with 99.78% confidence.

  How to Re-Train the Model (Google Colab)

Open PokemonGen1Classifier.ipynb in Google Colab.

The notebook contains all steps:

Download dataset from Kaggle

Build the model (MobileNetV2 transfer learning)

Train and evaluate

You can also load pokedex_model.keras and pokemon_class_names.npy from this repository and test them inside the notebook.

Dataset

This model was trained on the “First Gen Pokémon Classification” dataset from Kaggle.
