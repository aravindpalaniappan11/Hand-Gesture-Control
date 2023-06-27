import cv2
import mediapipe as mp
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
in_fi=[8]
cap = cv2.VideoCapture(0)
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
in_fi=[8]
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        
        success, image = cap.read()
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        results = hands.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:


                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
            xco=[]
            yco=[]
            for id,lms in enumerate(hand_landmarks.landmark):
                ih,iw,ic = image.shape
                x,y = int(lms.x*iw),int(lms.y*ih)
                xco.append(x)
                yco.append(y)

            if yco[17]>yco[18]>yco[19]>yco[20]:
                p = 'open'
            else:
                p = 'close'

            if yco[5]>yco[6]>yco[7]>yco[8]:
                i = 'open'
            else:
                i = 'close'
            
            if yco[13]>yco[14]>yco[15]>yco[16]:
                r = 'open'
            else:
                r = 'close'
                
            if (p and i) and (p and r) and (i and r) == 'open':
                cv2.putText(image,'Success',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255, 0, 0),2,cv2.LINE_AA)
            else:
                cv2.putText(image,'Failure',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255, 0, 0),2,cv2.LINE_AA)
            
        cv2.imshow('MediaPipe Hands', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()