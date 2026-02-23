from fastapi import FastAPI
import pickle
import numpy as np
import cv2
import mediapipe as mp
import threading

app = FastAPI()

#Carregar modelo
with open("modelo.pkl", "rb") as f:
    modelo = pickle.load(f)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

letra_atual = "?"

def camera_loop():
    global letra_atual

    cap = cv2.VideoCapture(0)

    with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7
    ) as hands:

        while True:
            ret, frame = cap.read()
            if not ret:
                continue

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(frame_rgb)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:

                    pontos = []
                    for lm in hand_landmarks.landmark:
                        pontos.append(lm.x)
                        pontos.append(lm.y)

                    pontos = np.array(pontos)
                    pred = modelo.predict([pontos])[0]
                    letra_atual = pred

            cv2.imshow("Camera IA", frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break

    cap.release()
    cv2.destroyAllWindows()

#Rodar camera 
threading.Thread(target=camera_loop, daemon=True).start()

@app.get("/predict")
def predict():
    return {"letra": letra_atual}