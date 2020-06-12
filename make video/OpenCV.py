import cv2

SIZE = 16
FPS = 20

paths = list("hero "+str(i)+".png" for i in range(0,22))
     
background = cv2.imread("map.png",cv2.IMREAD_UNCHANGED)
height, width, channels = background.shape

fourcc = cv2.VideoWriter_fourcc(*'xvid')
out = cv2.VideoWriter("output.avi", fourcc, FPS, (width, height))

pos_x = [SIZE*7, SIZE*7, SIZE*7, SIZE*7, 
         SIZE*7, SIZE*6, SIZE*5, SIZE*4,
         SIZE*4, SIZE*4, SIZE*4, SIZE*4,
         SIZE*4, SIZE*5, SIZE*6, SIZE*7,
         SIZE*7, SIZE*7, SIZE*7, SIZE*7,
         SIZE*7, SIZE*7, SIZE*7]

pos_y = [SIZE*13, SIZE*12, SIZE*11, SIZE*10,
         SIZE*10, SIZE*10, SIZE*10, SIZE*10,
         SIZE*10, SIZE*11, SIZE*12, SIZE*13,
         SIZE*13, SIZE*13, SIZE*13, SIZE*13,
         SIZE*13, SIZE*12, SIZE*11, SIZE*10,
         SIZE*10, SIZE*10, SIZE*10]
i = 0

for path in paths:
    sprite = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    alpha = sprite[:,:,3] / 255.0
    beta = 1.0 - alpha
    for j in range(int(FPS*0.8)): 
        frame = background.copy()
        for c in range(3):
            frame[pos_y[i]:pos_y[i]+SIZE, pos_x[i]:pos_x[i]+SIZE, c] = alpha * sprite[:,:,c] + beta * frame[pos_y[i]:pos_y[i]+SIZE, pos_x[i]:pos_x[i]+SIZE, c]
        out.write(frame[:,:,:3])
    i += 1


out.release()

