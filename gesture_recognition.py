import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands

# Gesture detection functions
def is_hand_open(landmarks):
    tip_ids = [4, 8, 12, 16, 20]
    for i in range(1, 5):
        if landmarks[tip_ids[i]].y > landmarks[tip_ids[i] - 2].y:
            return False
    return True

def is_hand_closed(landmarks):
    tip_ids = [4, 8, 12, 16, 20]
    for i in range(1, 5):
        if landmarks[tip_ids[i]].y < landmarks[tip_ids[i] - 2].y:
            return False
    return True

def is_two_fingers_up(landmarks):
    index_tip, middle_tip = 8, 12
    ring_tip, pinky_tip = 16, 20
    return (landmarks[index_tip].y < landmarks[index_tip - 2].y and
            landmarks[middle_tip].y < landmarks[middle_tip - 2].y and
            landmarks[ring_tip].y > landmarks[ring_tip - 2].y and
            landmarks[pinky_tip].y > landmarks[pinky_tip - 2].y)

def is_one_finger_up(landmarks):
    index_tip, middle_tip, ring_tip, pinky_tip = 8, 12, 16, 20
    return (landmarks[index_tip].y < landmarks[index_tip - 2].y and
            landmarks[middle_tip].y > landmarks[middle_tip - 2].y and
            landmarks[ring_tip].y > landmarks[ring_tip - 2].y and
            landmarks[pinky_tip].y > landmarks[pinky_tip - 2].y)

def is_pinky_finger_up(landmarks):
    index_tip, middle_tip, ring_tip, pinky_tip = 8, 12, 16, 20
    return (landmarks[pinky_tip].y < landmarks[pinky_tip - 2].y and
            landmarks[index_tip].y > landmarks[index_tip - 2].y and
            landmarks[middle_tip].y > landmarks[middle_tip - 2].y and
            landmarks[ring_tip].y > landmarks[ring_tip - 2].y)
