# Download the new dataset
!kaggle datasets download -d sehriyarmemmedli/glasses-vs-noglasses-dataset

# Unzip the file
!unzip -q glasses-vs-noglasses-dataset.zip

print("✅ 'Glasses vs No Glasses' dataset downloaded!")

# Let's check the new folder structure
!ls
