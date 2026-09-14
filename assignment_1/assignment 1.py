import cv2

def print_image_information(image):
    height, width, channels = image.shape

    print("Image Height: ", height)
    print("Image Width: ", width)
    print("Image Channels: ", channels)
    print("Size:", image.size)
    print("Data Type:", image.dtype)

image = cv2.imread("iris-1 (1).jpg")

print_image_information(image)




#part two
import cv2


cam = cv2.VideoCapture(0)


frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))


fps = cam.get(cv2.CAP_PROP_FPS)

with open("solutions/camera_outputs.txt", "w") as file:
    file.write("FPS : " + str(fps) + "\n")
    file.write("Frame Width : " + str(frame_width) + "\n")
    file.write("Frame Height : " + str(frame_height) + "\n")

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (frame_width, frame_height))

while True:
    ret, frame = cam.read()

    out.write(frame)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
out.release()
cv2.destroyAllWindows()