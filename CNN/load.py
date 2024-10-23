import os
import cv2
from PIL import Image
import numpy as np

data = []
labels = []

# LABELS
#---------------
# chameleon 0
# crocodile 1
# dragons 2
# iguana 3
# snake 4
# turtle 5

base_path = os.path.join(os.getcwd(), "CNN/data")

# Chameleon
chameleons = os.listdir(os.path.join(base_path, "chameleon"))
for x in chameleons:
    img_path = os.path.join(base_path, "chameleon", x)
    imag = cv2.imread(img_path)
    if imag is not None:
        imag = cv2.cvtColor(imag, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
        img_from_ar = Image.fromarray(imag, 'RGB')
        resized_image = img_from_ar.resize((50, 50))
        data.append(np.array(resized_image))
        labels.append(0)

# Crocodile
crocodiles = os.listdir(os.path.join(base_path, "crocodile"))
for x in crocodiles:
    img_path = os.path.join(base_path, "crocodile", x)
    imag = cv2.imread(img_path)
    if imag is not None:
        imag = cv2.cvtColor(imag, cv2.COLOR_BGR2RGB)
        img_from_ar = Image.fromarray(imag, 'RGB')
        resized_image = img_from_ar.resize((50, 50))
        data.append(np.array(resized_image))
        labels.append(1)

# Dragons
dragons = os.listdir(os.path.join(base_path, "dragons"))
for x in dragons:
    img_path = os.path.join(base_path, "dragons", x)
    imag = cv2.imread(img_path)
    if imag is not None:
        imag = cv2.cvtColor(imag, cv2.COLOR_BGR2RGB)
        img_from_ar = Image.fromarray(imag, 'RGB')
        resized_image = img_from_ar.resize((50, 50))
        data.append(np.array(resized_image))
        labels.append(2)

# Iguana
iguanas = os.listdir(os.path.join(base_path, "iguana"))
for x in iguanas:
    img_path = os.path.join(base_path, "iguana", x)
    imag = cv2.imread(img_path)
    if imag is not None:
        imag = cv2.cvtColor(imag, cv2.COLOR_BGR2RGB)
        img_from_ar = Image.fromarray(imag, 'RGB')
        resized_image = img_from_ar.resize((50, 50))
        data.append(np.array(resized_image))
        labels.append(3)

# Snake
snakes = os.listdir(os.path.join(base_path, "snake"))
for x in snakes:
    img_path = os.path.join(base_path, "snake", x)
    imag = cv2.imread(img_path)
    if imag is not None:
        imag = cv2.cvtColor(imag, cv2.COLOR_BGR2RGB)
        img_from_ar = Image.fromarray(imag, 'RGB')
        resized_image = img_from_ar.resize((50, 50))
        data.append(np.array(resized_image))
        labels.append(4)

# Turtle
turtles = os.listdir(os.path.join(base_path, "turtle"))
for x in turtles:
    img_path = os.path.join(base_path, "turtle", x)
    imag = cv2.imread(img_path)
    if imag is not None:
        imag = cv2.cvtColor(imag, cv2.COLOR_BGR2RGB)
        img_from_ar = Image.fromarray(imag, 'RGB')
        resized_image = img_from_ar.resize((50, 50))
        data.append(np.array(resized_image))
        labels.append(5)

# Convert data and labels to NumPy arrays
animals = np.array(data)
labels = np.array(labels)

# Save the arrays to disk
np.save("animals", animals)
np.save("labels", labels)
