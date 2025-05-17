import cv2


# Initialize the webcam (0 is the default camera)
video = cv2.VideoCapture(0)

if not video.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Press 'q' to exit.")

while True:
    # Capture frame-by-frame
    ret, frame = video.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Flip the frame horizontally to stop mirroring
    frame = cv2.flip(frame, 1)  # 1 indicates horizontal flipping

    # Display the resulting frame
    cv2.imshow("Webcam Feed", frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
video.release()
cv2.destroyAllWindows()
