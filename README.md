🤖 Hand Gesture to Voice Assistant using Gemini AI

This project is a real-time hand gesture recognition system that converts simple hand signs into natural spoken sentences using Google Gemini AI and text-to-speech.

It is especially useful for:

Assistive communication

Gesture-based interaction

Basic sign-to-speech systems

✨ Features

🖐️ Real-time hand detection using MediaPipe

🔢 Finger counting–based gesture recognition

🧠 Converts gestures into natural sentences using Gemini AI

🔊 Speaks the output using Text-to-Speech (pyttsx3)

🎥 Live webcam feed with gesture display

⏱️ Cool-down delay to avoid repeated speech

🛠️ Technologies Used

Python

OpenCV – Webcam handling & display

MediaPipe – Hand landmark detection

Google Gemini API – Natural language generation

pyttsx3 – Offline text-to-speech

NumPy

📁 Gesture Mapping
Fingers Shown	Gesture Meaning
0	Help
1	Yes
2	No
3	I need water
4	Hello

You can easily extend this mapping in the code.

📦 Installation
1️⃣ Clone the repository
git clone https://github.com/your-username/hand-gesture-gemini.git
cd hand-gesture-gemini

2️⃣ Install dependencies
pip install opencv-python mediapipe numpy pyttsx3 google-generativeai

🔑 Gemini API Setup

Go to Google AI Studio

Generate a Gemini API Key

Replace this line in the code:

genai.configure(api_key="YOUR_API_KEY_HERE")


⚠️ Do not expose your API key in public repositories

▶️ How to Run
python main.py


Show your hand in front of the camera

Hold a gesture for a moment

The system will recognize → convert → speak

Press ESC to exit

🧠 How It Works (Simple Explanation)

Webcam captures video frames

MediaPipe detects hand landmarks

Fingers are counted based on landmark positions

Each finger count maps to a gesture

Gemini AI converts the gesture meaning into a natural sentence

pyttsx3 speaks the sentence aloud
