import cv2
from pyzbar import pyzbar



cap = cv2.VideoCapture(0)



def camera():
    while True:
        # print("waiting for image ....")
        exit = 0
        ret, frame = cap.read()
        frame = cv2.resize(frame, (0, 0),fx=0.50, fy=0.50)	
        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
            barcodeData = barcode.data.decode("utf-8")
            barcodeType = barcode.type
            text = "{} ({})".format(barcodeData, barcodeType)
            print(text)
            # exit = 1

        cv2.imshow("Barcode Scanner",frame)
        if exit==0:
            if cv2.waitKey(1)==ord('q'):
                    break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()