from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from pyzbar.pyzbar import decode
from kivy.uix.label import Label
import cv2
import numpy

class BarcodeReader(App):
    def build(self):
        rtsp_url = 'http://192.168.2.124:8080/video'
        self.img1 = Image()
        layout = BoxLayout()
        layout.add_widget(self.img1)
        self.capture = cv2.VideoCapture(rtsp_url)
        Clock.schedule_interval(self.update, 1.0/33.0)
        return layout

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            detected_barcodes = decode(gray)
            if detected_barcodes:
                for barcode in detected_barcodes:
                    my_data = barcode.data.decode('utf-8')
                    print(my_data)
                    pts = numpy.array([barcode.polygon], numpy.int32)
                    pts = pts.reshape(-1, 1, 2)
                    cv2.polylines(frame, [pts], True, (255, 0, 255), 5)
                    pts2 = barcode.rect
                    cv2.putText(frame, my_data, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                                0.9, (255, 0, 255), 2)
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tostring()
            texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.img1.texture = texture1

    def on_stop(self):
        self.capture.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    BarcodeReader().run()