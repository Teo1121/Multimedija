import cv2
SIZE = 16
WIDTH = SIZE*8
HEIGHT = SIZE*3

img = cv2.imread("hero.png", cv2.IMREAD_UNCHANGED)

i = 0
for y in range(0,HEIGHT,SIZE):
    for x in range(0,WIDTH,SIZE):
        cv2.imwrite("./hero "+str(i)+".png",img[y:y+SIZE, x:x+SIZE])
        i += 1


