import cv2
import numpy as np

image = cv2.imread('./resources/input.jpg')

heigth, width = image.shape[:2]

quarter_height, quarter_width = heigth / 4, width / 4

#     | 1 0 Tx |
# T = | 0 1 Ty |

#Construcao da matriz de transposicao
T = np.float32( [[1,0,quarter_width], [0,1,quarter_height]] )

img_translation = cv2.warpAffine(image, T, (width, heigth))
cv2.imshow('Translation', img_translation)

print( T )

cv2.waitKey()
cv2.destroyAllWindows()