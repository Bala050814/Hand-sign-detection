import cv2
import google.generativeai as genai
import pyttsx3
import time
import mediapipe as mp
import numpy as np

# ---------------- GEMINI SETUP ----------------

import google.generativeai as genai

genai.configure(api_key="AIzaSyAhofjCvOsJ9_WDbgkBoLiGVy08Kz1nc_o")

model = genai.GenerativeModel("models/gemini-2.5-flash")

# ---------------- VOICE ----------------
engine = pyttsx3.init()

# ---------------- MEDIAPIPE ----------------
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hand_detector = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# ---------------- CAMERA ----------------
cap = cv2.VideoCapture(0)

# ---------------- GESTURE LOGIC ----------------
def count_fingers(hand_landmarks):
    tips = [8, 12, 16, 20]
    count = 0
    for tip in tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            count += 1
    return count

gesture_map = {
    0: "Help",
    1: "Yes",
    2: "No",
    3: "I need water",
    4: "Hello"
}

last_time = 0

print("Starting hand gesture recognition...")
print("Press 'ESC' to exit")

# ---------------- MAIN LOOP ----------------
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Cannot read frame")
        break
        
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hand_detector.process(rgb)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

            fingers = count_fingers(hand)
            gesture = gesture_map.get(fingers, None)

            if gesture and time.time() - last_time > 3:
                prompt = f"""
                A person shows a hand sign meaning '{gesture}'.
                Convert this into a short, natural sentence.
                """
try:
                    response = model.generate_content(prompt)
                    genai_text = response.text.strip()

                    print("Gesture:", gesture)
                    print("Gemini:", genai_text)

                    engine.say(genai_text)
                    engine.runAndWait()
                except Exception as e:
                    print(f"Error with Gemini: {e}")

                last_time = time.time()

            if gesture:
                cv2.putText(frame, gesture, (30, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0, 255, 0), 2)

    cv2.imshow("Hand Sign Recognition (Gemini)", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()
print("Application closed.")
