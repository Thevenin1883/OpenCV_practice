import cv2

vfile = cv2.VideoCapture(0)

if vfile.isOpened():
    while True:
        vret, img = vfile.read()
        if vret: # vret값이 들어 오는 동안 
            cv2.imshow('webcam', img) #이미지를 가져오고 
            if cv2.waitKey(1) != -1:
                cv2.imwrite('webcam_snap.jpg', img)
                break
        else:
            print("프레임이 정상적이지 않음")
            break
else:
    print ("Error")

vfile.release()
cv2.destroyAllWindows()