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
