
#edge detection
import cv2
import numpy as np

image = cv2.imread("lambo.png")

def sobel_edge(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred_image = cv2.GaussianBlur(gray_image, (3,3), 0)

    sobel_image = cv2.Sobel(blurred_image, cv2.CV_64F, 1, 1, ksize=1)

    return sobel_image

sobel_image = sobel_edge(image)
cv2.imwrite("solutions/sobel_image.png", sobel_image)

#canny edge detection

def canny_edge(image, threshold1, threshold2):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    blurred_image = cv2.GaussianBlur(image, (3,3), 0)

    canny_image = cv2.Canny(blurred_image, threshold1, threshold2)

    return canny_image

canny_image = canny_edge(image, 50, 50)

cv2.imwrite("solutions/canny_image.png", canny_image)



#template matching
def templatematch(image, template):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(
        gray_image,
        gray_template,
        cv2.TM_CCOEFF_NORMED
    )

    threshold = 0.9

    location = np.where(result >= threshold)

    height, width = gray_template.shape

    for point in zip(*location[::-1]):
        cv2.rectangle(
            image, point, (point[0] + width, point[1] + height), (0, 0, 255), 2)

    return image

shapes_image = cv2.imread("shapes.png")
template = cv2.imread("shapes_template.jpg")

matched_image = templatematch(shapes_image, template)

cv2.imwrite("solutions/matched_image.png", matched_image)


#resizing

def resize(image, scale_factor: int, up_or_down: str):
    resized_image = image

    if up_or_down == "up":
        for i in range(scale_factor):
            resized_image = cv2.pyrUp(resized_image)
    elif up_or_down == "down":
        for i in range(scale_factor):
            resized_image = cv2.pyrDown(resized_image)
    return resized_image

resizedup = resize(image, 2, "up")
resizeddown = resize(image, 2, "down")

cv2.imwrite("solutions/resizedup.png", resizedup)
cv2.imwrite("solutions/resizeddown.png", resizeddown)
