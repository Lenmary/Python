import cv2 # descargar el paquete de opencv2
imagen = cv2.imread('pics/paisaje.jpg',0) # cambiar el valor entero por 0
cv2.imshow('paisaje',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()