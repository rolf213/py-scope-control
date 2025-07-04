import mediapipe as mp
import cv2
import numpy as np
import uuid #random string zapisywanie
import os
import HandshapeRecognizer as hr

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
#mp_drawing_styles = mp.solutions.drawing_styles

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

frameWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frameHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
handshapeRecognizer = hr.HandshapeRecognizer("Models")

#DETECTION - POCZATKOWA, TRACKING - SLEDZACA / max_num_hands=4 zwieksza liczbe rak
with mp_hands.Hands(model_complexity=1,min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()

        #recolor - nie dziala - lekki negatyw

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #image = frame

        #jakby nie działało to te flagi do zmiany
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True

        #image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        #wyniki skany ()
        #print(results.multi_hand_world_landmarks)

        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS, 
                mp_drawing.DrawingSpec(color=(121,22,76),thickness=2,circle_radius=4),
                mp_drawing.DrawingSpec(color=(121,44,76),thickness=2,circle_radius=2))
				
        predictedLabel = handshapeRecognizer.run(results, frameWidth, frameHeight)
        print(predictedLabel)

        #cv2.imwrite(
        #    os.path.join(
        #        'Wyniki',
        #        '{}.jpg'.format(uuid.uuid1())),
        #    image)
        
        cv2.imshow('Camera', frame)

        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()
cv2.destroyAllWindows()
