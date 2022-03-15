from threading import Thread
from VideoGet import VideoGet
from datetime import date
from pathlib import Path
import argparse
import cv2

today = date.today()
today_str = today.strftime("%d_%m_%Y")

n_cameras = 8

video_get_v = [None] * n_cameras
window_title_v = [None] * n_cameras
out_v = [None] * n_cameras

fourcc = cv2.VideoWriter_fourcc(*'XVID')

for i in range(0, n_cameras):

    window_title_v[i] = f"camera {i+1}"

    file_name = '_'.join([today_str, f"cam_{i+1}"])

    c = 1
    while Path("./" + file_name + ".avi").is_file():
        file_name = '_'.join([today_str, f"cam_{c*n_cameras + i + 1}"])

        window_title_v[i] = f"camera {c*n_cameras + i + 1}"
        
        c += 1
  
    cv2.namedWindow(window_title_v[i], cv2.WINDOW_NORMAL)

    out_stream = cv2.VideoWriter(file_name + ".avi", fourcc, 30, (640, 480))

    video_get_v[i] = VideoGet(out_stream, i)
    video_get_v[i].start()


while True:

    if (cv2.waitKey(1) == ord("q")):
        for i in range(0, n_cameras):
            video_get_v[i].stop()
        break

    for i in range(0, n_cameras):
        frame = video_get_v[i].frame

        cv2.imshow(window_title_v[i], frame)

cv2.destroyAllWindows()