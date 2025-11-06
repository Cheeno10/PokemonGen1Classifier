from google.colab import files

# Run this and upload your kaggle.json file
uploaded = files.upload()

if 'kaggle.json' in uploaded:
  print("Kaggle.json uploaded!")
  # Set up the API token
  !pip install -q kaggle
  !mkdir -p ~/.kaggle
  !cp kaggle.json ~/.kaggle/
  !chmod 600 ~/.kaggle/kaggle.json
else:
  print("Please upload your kaggle.json file")
