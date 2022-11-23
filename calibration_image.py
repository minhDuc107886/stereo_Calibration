import cv2

capL = cv2.VideoCapture(1)
capR = cv2.VideoCapture(2)

num = 0

while capL.isOpened():

    succes1, imgL = capL.read()
    succes2, imgR = capR.read()

    k = cv2.waitKey(5)

    if k == 27:
        break
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite('img_detect/imgL' + str(num) + '.png', imgL)
        cv2.imwrite('img_detect/imgR' + str(num) + '.png', imgR)
        print("images saved!")
        num += 1

    cv2.imshow('Img L',imgL)
    cv2.imshow('Img R',imgR)

# Release and destroy all windows before termination
capL.release()
capR.release()

cv2.destroyAllWindows()