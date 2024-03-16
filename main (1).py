import cv2 as cv
import streamlit as st
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Part 1 - Read the image file and store it. Gray scale image with thresh binary.
original_image = cv.imread('signature.jpg')
gray_scale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)
if original_image is None:
    print("ERROR: Unable to read image")

# Part 2 - Remove background by thresholding the gray scale image
_, remove_background_image = cv.threshold(gray_scale_image, 100, 255, cv.THRESH_BINARY)

# Part 3 - Save all versions of the images (original, grayscale, remove background) --> save images as .png file
cv.imwrite("original_image.png", original_image)
cv.imwrite("gray_scale_image.png", gray_scale_image)
cv.imwrite("remove_background_image.png", remove_background_image)

# Part 4 - Make image transparent
rgba = cv.cvtColor(original_image, cv.COLOR_BGR2BGRA)
image_with_intensity_values = cv.cvtColor(rgba, cv.COLOR_BGR2GRAY)
(T, thresh) = cv.threshold(image_with_intensity_values, 120, 255, cv.THRESH_BINARY)
rgba[:, :, 3] = np.where(thresh == 255, 0, 255)

cv.imwrite("transparent_image.png", rgba)

# Display all versions of the images (original, grayscale, remove background, transparent)
cv.imshow('Original Image', original_image)
cv.imshow('Grayscale Image', gray_scale_image)
cv.imshow('Remove Background Image', remove_background_image)
cv.imshow('Transparent Image', thresh)

# Part 5 - Implementing Streamlit for the 2 GUI elements
st.title("OpenCV Signature Project - App")
st.subheader("This app will play with the versions of the images we made through the 2 GUI elements")
st.text("Integration of Python OpenCV and Streamlit in this app")

image1 = Image.open("C:\\Users\\jshri\\PycharmProjects\\OpenCV Signature Project\\original_image.png")
st.image(image1, caption="Original Image")
picture = st.camera_input("Smile! :)")
if picture:
    st.image(picture)

image2 = Image.open("C:\\Users\\jshri\\PycharmProjects\\OpenCV Signature Project\\gray_scale_image.png")
st.image(image2, caption="Grayscale Image")
with open("C:\\Users\\jshri\\PycharmProjects\\OpenCV Signature Project\\gray_scale_image.png", "rb") as file:
    btn = st.download_button(
        label="Download Image",
        data=file.read(),
        file_name="downloaded_image.png",
        mime="image/png"
    )

image3 = Image.open("C:\\Users\\jshri\\PycharmProjects\\OpenCV Signature Project\\remove_background_image.png")
st.image(image3, caption="Remove Background Image")

image4 = Image.open("C:\\Users\\jshri\\PycharmProjects\\OpenCV Signature Project\\transparent_image.png")
st.image(image4, caption="Transparent Image")
uploaded_files = st.file_uploader("Input a new Signature", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

cv.waitKey(0)

# ENTER INTO TERMINAL:  streamlit run main.py
