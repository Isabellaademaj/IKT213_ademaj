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

#åpner default kamera
cam = cv2.VideoCapture(0)

#default frame width and height
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

#fps
fps = cam.get(cv2.CAP_PROP_FPS)

with open("solutions/camera_outputs.txt", "w") as file:
    file.write("FPS : " + str(fps) + "\n")
    file.write("Frame Width : " + str(frame_width) + "\n")
    file.write("Frame Height : " + str(frame_height) + "\n")


#definind the coed and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (frame_width, frame_height))

while True:
    ret, frame = cam.read()

# write the frame to the output file
    out.write(frame)

# Display the captured frame
    cv2.imshow('frame', frame)

#press q to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# release the capture and writer objects
cam.release()
out.release()
cv2.destroyAllWindows()