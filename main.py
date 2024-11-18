import cv2
import time
import argparse
from gesture_recognition import is_hand_open, is_hand_closed, is_two_fingers_up, is_one_finger_up, is_pinky_finger_up
from vlc_controller import handle_gesture as vlc_handle_gesture
from spotify_controller import play_spotify, pause_spotify, next_track, volume_up, volume_down
import mediapipe as mp

# Command-line argument parsing
parser = argparse.ArgumentParser(description="Control VLC or Spotify using hand gestures.")
parser.add_argument('--mode', choices=['vlc', 'spotify'], required=True, help="Choose between 'vlc' or 'spotify' mode.")
args = parser.parse_args()

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(0)

# Gesture cooldown settings
last_gesture_time = time.time()
gesture_cooldown = 5  # 5 seconds cooldown between gestures

def handle_spotify_gesture(gesture):
    """Handle gestures for Spotify control."""
    if gesture == "Open Hand":
        play_spotify()
    elif gesture == "Closed Fist":
        pause_spotify()
    elif gesture == "Two Fingers Up":
        next_track()
    elif gesture == "One Finger Up":
        volume_up()
    elif gesture == "Pinky Finger Up":
        volume_down()

# Start MediaPipe Hands with a single hand detection
with mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Determine the gesture
                if is_hand_open(hand_landmarks.landmark):
                    gesture = "Open Hand"
                elif is_hand_closed(hand_landmarks.landmark):
                    gesture = "Closed Fist"
                elif is_two_fingers_up(hand_landmarks.landmark):
                    gesture = "Two Fingers Up"
                elif is_one_finger_up(hand_landmarks.landmark):
                    gesture = "One Finger Up"
                elif is_pinky_finger_up(hand_landmarks.landmark):
                    gesture = "Pinky Finger Up"
                else:
                    gesture = None

                # Handle gesture if enough time has passed since the last action
                if gesture and (time.time() - last_gesture_time > gesture_cooldown):
                    if args.mode == 'spotify':
                        handle_spotify_gesture(gesture)
                    elif args.mode == 'vlc':
                        vlc_handle_gesture(gesture)

                    last_gesture_time = time.time()

                # Display the detected gesture
                if gesture:
                    cv2.putText(frame, f"{gesture} Detected", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

        # Display the frame
        cv2.imshow("Gesture Control", frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
