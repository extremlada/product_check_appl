import cv2
import requests
from pyzbar.pyzbar import decode
from bs4 import BeautifulSoup
import numpy
from MySql_dumb import *

def barcode_readin():
# where i connect to the ip webcam
    global barcode_found
    global myData
    rtsp_url = 'http://192.168.0.127:8080/video'
    window_name = 'OpenCV Barcode'

    bd = cv2.barcode.BarcodeDetector()
    cap = cv2.VideoCapture(rtsp_url)
    cap.set(3, 640)
    cap.set(4, 480)

# infinite loop for the webcam so it can read everytime a barcode is on the screen (not efficient but it works XD)barcode_found = False
    barcode_found = False
    while True:
        ret, frame = cap.read()
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
            barcode_found = True
            return [myData]
    # will show in a separate window
        cv2.imshow(window_name, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break  # Break the loop if 'q' is pressed



def lookup_barcodes(barcode_data):
    if barcode_data:
        barcode = barcode_data[0]  # Get the first element (barcode data)
        api_key = "D609027EA3150ED57818C5D1CB3E1BC8"
        url = f"https://api.upcdatabase.org/product/{barcode}?apikey={api_key}"
        response = requests.get(url)
        data = response.json()
        if 'title' in data:
            print("Product Name:", data['title'])
            print("Description:", data['description'])
            print("Brand:", data['brand'])
            print("Category:", data.get('category', 'Not available'))
            print("Nutritions: ", data['metanutrition'])
            barcode = data['barcode']
            name = data['title']
            category = data['category']
            metadata = "asd"
            metanutritions = "asd"
            brand = data['brand']
            commit_mysql(barcode,  name, category, metadata, metanutritions, brand)

        else:
            print("Barcode not found.")
    else:
        print("No barcode data provided.")

