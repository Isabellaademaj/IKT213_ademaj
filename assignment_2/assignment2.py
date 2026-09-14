import cv2
import numpy as np

image = cv2.imread("iris-1.png")

def padding(image, border_width):
    padded_image = cv2.copyMakeBorder(
        image,
        border_width,
        border_width,
        border_width,
        border_width,
        cv2.BORDER_REFLECT
    )

    return padded_image

padded_image = padding(image, 100)
cv2.imwrite("solutions/padded_image.png", padded_image)


#iii

def crop(image, x_0, x_1, y_0, y_1):
    cropped_image = image[y_0:y_1, x_0:x_1]
    return cropped_image

height, width = image.shape[:2]

cropped_image = crop(image, 200, width - 130, 200, height -130)

cv2.imwrite("solutions/cropped_image.png", cropped_image)

#iii
def resize(image, width, height):
    resized_image = cv2.resize(image, (width, height))
    return resized_image

resized_image = resize(image, 200, 200)
cv2.imwrite("solutions/resized_image.png", resized_image)


#iiii
height, width, channels = image.shape

EmptyPictureArray = np.zeros((height, width, 3), dtype = np.uint8)

def copy(image, empty_picture_array):
    for y in range(height):
        for x in range(width):
            empty_picture_array[y, x] = image[y, x]

    return empty_picture_array

copied_image = copy(image, EmptyPictureArray)

cv2.imwrite("solutions/copied_image.png", copied_image)


#Grayscale

def grayscale(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

gray_image = grayscale(image)

cv2.imwrite("solutions/gray_image.png", gray_image)


#HSV

def hsv(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    return hsv_image

hsv_image = hsv(image)
cv2.imwrite("solutions/hsv_image.png", hsv_image)

#color shifting
def hue_shifted(image, EmptyPictureArray, hue):
    height, width, channels = image.shape

    for y in range(height):
        for x in range(width):
            for c in range(channels):
                value = int(image[y, x, c]) + hue

                if value > 255:
                    value = 255
                elif value < 0:
                    value = 0

                EmptyPictureArray[y, x, c] = value

    return EmptyPictureArray

EmptyPictureArray = np.zeros(image.shape , dtype = np.uint8)

shifted_image = hue_shifted(image, EmptyPictureArray, 50)

cv2.imwrite("solutions/shifted_image.png", shifted_image)

#smoothing

def smoothing(image):
    smoothed_image = cv2.GaussianBlur(image, (15, 15), 0, borderType=cv2.BORDER_DEFAULT)

    return smoothed_image

smoothed_image = smoothing(image)

cv2.imwrite("solutions/smoothed_image.png", smoothed_image)


#rotation

def rotation(image, rotation_angle):
    if rotation_angle == 90:
        rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    elif rotation_angle == 180:
        rotated_image = cv2.rotate(image, cv2.ROTATE_180)

    return rotated_image

rotated_image = rotation(image, 180)
cv2.imwrite("solutions/rotated_image.png", rotated_image)