import os
import random
import shutil

# Set the dataset path
dataset_path = "D:/MyWorkspace/StudyProjectCameraTrapChallenge/ObjectDetectionWithCustomYoloV7/data"

# Set the train, test, val split ratios
train_ratio = 0.8
test_ratio = 0.1
val_ratio = 0.1

# Get the list of image and label files
image_files = os.listdir(os.path.join(dataset_path, "images"))
label_files = os.listdir(os.path.join(dataset_path, "labels"))
num_images = len(image_files)

# Shuffle the image and label files together
combined_files = list(zip(image_files, label_files))
random.shuffle(combined_files)

# Calculate the split points
train_split = int(num_images * train_ratio)
test_split = int(num_images * (train_ratio + test_ratio))

# Create the train, test, and val directories if they don't already exist
for split_dir in ["train", "test", "val"]:
    os.makedirs(os.path.join(dataset_path, split_dir, "images"), exist_ok=True)
    os.makedirs(os.path.join(dataset_path, split_dir, "labels"), exist_ok=True)

# Copy the images and labels to their respective train, test, and val directories
for i, (image_file, label_file) in enumerate(combined_files):
    # Determine the destination directory based on the split ratio
    if i < train_split:
        split_dir = "train"
    elif i < test_split:
        split_dir = "test"
    else:
        split_dir = "val"

    # Copy the image file to the appropriate split directory
    shutil.copyfile(os.path.join(dataset_path, "images", image_file),
                    os.path.join(dataset_path, split_dir, "images", image_file))

    # Copy the label file to the appropriate split directory
    shutil.copyfile(os.path.join(dataset_path, "labels", label_file),
                    os.path.join(dataset_path, split_dir, "labels", label_file))

# Get the updated list of image and label files
image_files = os.listdir(os.path.join(dataset_path, "images"))
label_files = os.listdir(os.path.join(dataset_path, "labels"))

print(image_files)
print(label_files)
