import cv2
import mediapipe as mp
import pyautogui as p

cap=cv2.VideoCapture(0)
tips=[4,8,12,16,20]
mpHands= mp.solutions.hands
hands=mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

def findHands(img, draw=True):
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            if draw:
                mpDraw.draw_landmarks(img, handLms,mpHands.HAND_CONNECTIONS)
    return  img


def findposition(img, handNo=0, draw=True):
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    lst=[]
    if results.multi_hand_landmarks:
        myHand = results.multi_hand_landmarks[handNo]
        for id, lm in enumerate(myHand.landmark):
            # print(id, lm)
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            # print(id, cx, cy)
            lst.append([id, cx, cy])
            # if draw:
                # cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

    return lst
def control(count):
    switcher = {
        0: 'F',
        1: 'right',
        2: 'left',
        3: 'up',
        4: 'down',
        5: 'space',
    }
    return switcher.get(count)

while True:
    success,img = cap.read()
    img=cv2.flip(img,2)
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = findHands(img, draw=True)
    lm=findposition(img)
    # results = hands.process(imgRGB)
    if len(lm)!=0:
        finger_open=[]
        if (lm[tips[0]][1]<lm[tips[0]-1][1]):
            finger_open.append(1)
        else:
            finger_open.append(0)

        for id in range(1,5):
            if(lm[tips[id]][2]<lm[tips[id]-1][2]):
                finger_open.append(1)
            else:
                finger_open.append(0)
        count=finger_open.count(1)
        print(finger_open)
        c=control(count)
        p.press(c)
    cv2.imshow("Image",img)
    cv2.waitKey(1)
