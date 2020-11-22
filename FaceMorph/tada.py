import cv2
import numpy as np
import dlib

# Load the detector
detector = dlib.get_frontal_face_detector()

# Load the predictor
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# read the image
img = cv2.imread("bonoro.jpg")

    

# Convert image into grayscale
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

# Use detector to find landmarks
faces = detector(gray)
for face in faces:
    x1 = face.left() # left point
    y1 = face.top() # top point
    x2 = face.right() # right point
    y2 = face.bottom() # bottom point

    # Create landmark object
    landmarks = predictor(image=gray, box=face)

    
    points = []
    # Loop through all the points
    for n in range(0, 68):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
    
        
        points.append([x,y])
    
    points_bordo =  [[437 ,230],[270, 680],[0, 460],[599 ,420],[0, 0],[0 ,230],[0 ,799],[300, 799],[599, 799],[599, 230],[599, 0],[300, 0]]
    
    for i in points_bordo:
        points.append(i)
    
    for n in points:
        x = n[0]
        y = n[1]
        
        # Draw a circle
        cv2.circle(img=img, center=(x, y), radius=3, color=(0,0, 255), thickness=-1)

def write_txt(conteudo, filename):
      points = []
      for i in range(len(conteudo)):
          if i != (len(conteudo)-1):
              points.append(f"{conteudo[i][0]} {conteudo[i][1]}\n")
          else:
              points.append(f"{conteudo[i][0]} {conteudo[i][1]}")
           
      arquivo = open(filename + ".txt", 'w') 
      arquivo.writelines(points)
      arquivo.close()
     
write_txt(points, "bonoro.jpg")

# show the image
cv2.imshow(winname="Face", mat=img)

# Delay between every fram
cv2.waitKey(delay=0)

# Close all windows
cv2.destroyAllWindows()

