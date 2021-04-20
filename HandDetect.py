import cv2
import pyautogui
import mediapipe as mp
import math
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

def distance(x1, x2, y1, y2):
  distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
  return distance

def detector():
  cap = cv2.VideoCapture(0)
  with mp_hands.Hands(
      min_detection_confidence=0.5,
      max_num_hands=1,
      min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
      success, image = cap.read()
      if not success:
        print("Ignoring empty camera frame.")
        continue

      image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

      image.flags.writeable = False
      results = hands.process(image)

      image.flags.writeable = True
      image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
      
      if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
          x, y = int(hand_landmarks.landmark[0].x*image.shape[1]) ,int(hand_landmarks.landmark[0].y*image.shape[0])
          # print(x, y)
          
          x1 , y1 = hand_landmarks.landmark[4].x*1920 ,hand_landmarks.landmark[4].y*1080
          x2 , y2 = hand_landmarks.landmark[8].x*1920 ,hand_landmarks.landmark[8].y*1080
          x0 , y0 = hand_landmarks.landmark[0].x*image.shape[1] ,hand_landmarks.landmark[0].y*image.shape[0]
          x5 , y5 = hand_landmarks.landmark[5].x*image.shape[1] ,hand_landmarks.landmark[5].y*image.shape[0]
          x17 , y17 = hand_landmarks.landmark[17].x*image.shape[1],hand_landmarks.landmark[17].y*image.shape[0]
          midx,midy = int((x0+x5+x17)/3), int((y0+y5+y17)/3)
          cv2.circle(image, (midx, midy), 10, (255, 0, 255), cv2.FILLED)
          pyautogui.moveTo(midx*1920/image.shape[1], midy*1080/image.shape[0])
          print(distance(x1,x2,y1,y2))

          if distance(x1,x2,y1,y2) <= 70:
            pyautogui.click()

          mp_drawing.draw_landmarks(
              image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        # print(results.multi_hand_landmarks)  
      cv2.imshow('MediaPipe Hands', image)
      if cv2.waitKey(5) & 0xFF == 27: # ESC to exit
        break
  cap.release()
  # print(mp_hands.data.Hands.landmarks[0])