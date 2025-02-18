import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe utilities
drawing_utils = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
screen_width, screen_height = pyautogui.size() 

index_y = 0


# Initialize hand detector
hand_detector = mp_hands.Hands()

# Initialize video capture (Use 0 for the default camera)
capa = cv2.VideoCapture(1)

while capa.isOpened():
    ret, virtualMouse = capa.read()
    if not ret:
        break
    
    # Flip the frame horizontally for a natural mirroring effect
    frame = cv2.flip(virtualMouse, 1)

    # Convert the frame to RGB for MediaPipe
    rgb_frame = cv2.cvtColor(virtualMouse, cv2.COLOR_BGR2RGB)

    # Process the frame to detect hands
    output = hand_detector.process(rgb_frame)

    # Get the detected hand landmarks
    hands = output.multi_hand_landmarks

    # Check if any hands were detected
    if hands:
        for hand_landmarks in hands:
            # Draw the hand landmarks on the frame
            drawing_utils.draw_landmarks(virtualMouse, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Iterate over each landmark in the detected hand
            for id, landmark in enumerate(hand_landmarks.landmark):
                h, w, _ = frame.shape  # Get frame dimensions
                cx, cy = int(landmark.x * w), int(landmark.y * h)  # Convert to pixel coordinates
                print(f"ID: {id}, X: {cx}, Y: {cy}")
                if id == 8 :


                # Draw a small circle on each landmark
                    cv2.circle(img=virtualMouse, center=(cx,cy), radius=15, color=(0, 255, 255))
                    index_x = screen_width/w *cx
                    index_y = screen_height/h *cy
                    pyautogui.moveTo(index_x,index_y)

                if id == 4 :


                # Draw a small circle on each landmark
                    cv2.circle(img=virtualMouse, center=(cx,cy), radius=15, color=(0, 255, 255))
                    thumb_x = screen_width/w *cx
                    thumb_y = screen_height/h *cy
                    print(int(abs(index_y-thumb_y)))
                    if abs(index_y-thumb_y) < 25 :
                        print('click')
                        

                        pyautogui.click()
                        pyautogui.sleep(1)

                    

    # Display the frame
    cv2.imshow('Hand Tracking', virtualMouse)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
capa.release()
cv2.destroyAllWindows()
