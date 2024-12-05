import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape
    
    cx = int(width / 2)
    cy = int(height / 2)
    
    # Valeur du pixel
    pixel_center = hsv_frame[cy, cx]
    hue_value = pixel_center[0]
    saturation_value = pixel_center[1]
    value = pixel_center[2]
    
    color = "Undefined"
    bgr_color = (0, 0, 0)  # Valeur par défaut en noir
    
    # Vérifier si la couleur est noire ou blanche
    if saturation_value == 0:
        if value == 0:
            color = "Noir"
            bgr_color = (0, 0, 0)  # Noir en BGR
        else:
            color = "Blanc"
            bgr_color = (255, 255, 255)  # Blanc en BGR
    elif hue_value < 5 or hue_value >= 170:
        color = "Rouge"
        bgr_color = (0, 0, 255)  # Rouge en BGR
    elif hue_value < 22:
        color = "Orange"
        bgr_color = (0, 165, 255)  # Orange en BGR
    elif hue_value < 31:
        color = "Jaune"
        bgr_color = (0, 255, 255)  # Jaune en BGR
    elif hue_value < 78:
        color = "Vert"
        bgr_color = (0, 255, 0)  # Vert en BGR
    elif hue_value < 131:
        color = "Bleu"
        bgr_color = (255, 0, 0)  # Bleu en BGR
    elif hue_value < 170:
        color = "Violet"
        bgr_color = (255, 0, 255)  # Violet en BGR
    
    # Afficher le nom de la couleur avec la couleur de fond du pixel
    cv2.putText(frame, color, (20, 100), 0, 1.5, bgr_color, 2)
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)  # Cercle au centre

    # Afficher l'image
    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
