import cv2
import numpy
from pyzbar.pyzbar import decode

camera_id = 0
delay = 1
rtsp_url = 'http://192.168.0.127:8080/video'
window_name = 'OpenCV Barcode'

bd = cv2.barcode.BarcodeDetector()
cap = cv2.VideoCapture(rtsp_url)
cap.set(3, 640)
cap.set(4, 480)


while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGBA2GRAY)
    for barcode in decode(gray):
        myData = barcode.data.decode('utf-8')
        print(myData)
        pts = numpy.array([barcode.polygon], numpy.int32)
        pts = pts.reshape(-1, 1, 2)
        cv2.polylines(gray, [pts], True, (255, 0, 255), 5)
        pts2 = barcode.rect
        cv2.putText(gray, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, (255, 0, 255), 2)

    cv2.imshow(window_name, gray)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()


# just incase i need this back because i fuck up
img = cv2.imread(image)
if img is None:
    print("Error: Image not found or cannot be read.")
    return None

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Decode the barcodes
detectedBarcodes = decode(gray_img)

if not detectedBarcodes:
    print("barcode is not detected or your barcode is blank/corrupted")
    return None
else:
    barcode_data = []
    for barcode in detectedBarcodes:
        barcode_data.append((barcode.data, barcode.type))
        (x, y, w, h) = barcode.rect

        cv2.rectangle(img, (x - 10, y - 10),
                      (x + w + 10, y + h + 10),
                      (255, 0, 0), 2)
        if barcode.data != "":
            print(barcode.data)
            print(barcode.type)

cv2.imshow("Image", img)
cv2.waitKey(2)
cv2.destroyAllWindows()

return barcode_data

# if i need this
def barcode_readin(image):
# where i connect to the ip webcam

    global myData
    rtsp_url = 'http://192.168.0.127:8080/video'
    window_name = 'OpenCV Barcode'

    bd = cv2.barcode.BarcodeDetector()
    cap = cv2.VideoCapture(rtsp_url)
    cap.set(3, 640)
    cap.set(4, 480)

# infinite loop for the webcam so it can read everytime a barcode is on the screen (not efficient but it works XD)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture frame")
            break
        # grey scaling the image of the webcam so it can read it better and
        # will not have any problem with the lighting
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detectedBarcodes = decode(gray)


        # will itarate through all of the images it will see on the screen
        for barcode in decode(gray):
            myData = barcode.data.decode('utf-8')
            print(myData)
            # just the math for the polygon so it will have a polygon over the barcode
            pts = numpy.array([barcode.polygon], numpy.int32)
            pts = pts.reshape(-1, 1, 2)
            cv2.polylines(gray, [pts], True, (255, 0, 255), 5)
            pts2 = barcode.rect
            cv2.putText(gray, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                        0.9, (255, 0, 255), 2)
            cv2.imshow(window_name, frame)
            cv2.waitKey(0)  # Wait for a key press
            cv2.destroyAllWindows()
            return [myData]
    # will show in a separate window
        cv2.imshow(window_name, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break  # Break the loop if 'q' is pressed


# kellhet az apphoz


    def build(self):
        self.img1=Image()
        layout = BoxLayout()
        layout.add_widget(self.img1)
        #opencv2 stuffs
        self.capture = cv2.VideoCapture(0)
        cv2.namedWindow("CV2 Image")
        Clock.schedule_interval(self.update, 1.0/33.0)
        return layout
