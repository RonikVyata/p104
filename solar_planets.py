import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Mercury",
            (100,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Venus",
            (200,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (243,25,25)
            )

cv2.putText(img,
            "Earth",
            (300,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,12,255)
            )

cv2.putText(img,
            "Mars",
            (400,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (223,155,45)
            )

cv2.putText(img,
            "Jupiter",
            (550,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,23)
            )

cv2.putText(img,
            "Saturn",
            (800,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (100,4,255)
            )

cv2.putText(img,
            "Uranus",
            (950,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,255,255)
            )

cv2.putText(img,
            "Neptune",
            (1100,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,0)
            )

cv2.imshow("output",img)

cv2.imwrite("Solar_systemwithname.jpg",img)

cv2.waitKey(0)

