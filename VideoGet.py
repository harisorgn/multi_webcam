from threading import Thread
import cv2


class VideoGet:

    def __init__(self, out_stream, src=0):
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.out_stream = out_stream
        self.stopped = False

    def start(self):    
        Thread(target=self.get, args=()).start()
        return self

    def get(self):
        while not self.stopped:
            if not self.grabbed:
                self.stop()
            else:
                (self.grabbed, self.frame) = self.stream.read()

                #b = cv2.resize(self.frame,(1280,720),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)

                self.out_stream.write(self.frame)

    def stop(self):
        self.stopped = True