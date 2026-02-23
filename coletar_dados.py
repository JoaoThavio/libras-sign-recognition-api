import cv2
import mediapipe as mp
import numpy as np
import os

#Letra coletada
LETRA = "A"  
TOTAL_AMOSTRAS = 300

#Salvar coleta
os.makedirs(f"dados/{LETRA}", exist_ok=True)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

contador = 0

with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
) as hands:

    while contador < TOTAL_AMOSTRAS:
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:

                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS
                )

                pontos = []
                for lm in hand_landmarks.landmark:
                    pontos.append(lm.x)
                    pontos.append(lm.y)

                np.save(
                    f"dados/{LETRA}/{LETRA}_{contador}.npy",
                    np.array(pontos)
                )

                contador += 1

        cv2.putText(
            frame,
            f"Letra: {LETRA}",
            (10, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Amostras: {contador}/{TOTAL_AMOSTRAS}",
            (10, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 0, 0),
            2
        )

        cv2.imshow("Coleta de Dados", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()

print("Coleta finalizada!!!")