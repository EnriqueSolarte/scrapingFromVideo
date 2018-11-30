import cv2
import os
import argparse
import datetime
import time


def get_frigerprint():
    date = datetime.datetime.now()
    fprint = date.year.__str__() + date.month.__str__() + date.day.__str__()
    fprint = fprint + "_" + date.hour.__str__() + date.minute.__str__() + date.second.__str__()

    return fprint


main_path = os.path.dirname(os.path.abspath(__file__))

parser = argparse.ArgumentParser(description='')
parser.add_argument('--video', dest='video', default=main_path + '/data/example.mp4',
                    help='video from which the dataset will be collected')
parser.add_argument('--dest', dest='dataset', default=main_path + '/dataset',
                    help='Destine where the images are stored')
parser.add_argument('--skipFrames', dest='skip', default=0, type=int,
                    help='number of frames which would be skipped')
parser.add_argument('--delay', dest='delay', default=0, type=int,
                    help='delay between frames in seconds')

args = parser.parse_args()
folder_destination = args.dataset


def click(event, x, y, t, p):
    if event == cv2.EVENT_LBUTTONDOWN:
        name = get_frigerprint()
        cv2.imwrite('{}/{}.jpg'.format(folder_destination, name), image)
        print('A picture {}.jpg has been captured...'.format(name))


video_name = args.video

cap = cv2.VideoCapture(video_name)
cv2.namedWindow("image")
cv2.setMouseCallback("image", click)

print("Scraping from video is running...")

aux = 0;
while True:
    ret, image = cap.read()
    if not ret:
        break

    if aux < args.skip:
        aux = aux + 1
        continue
    else:
        aux = 0

    # if the `q` key was pressed, break from the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

    cv2.imshow("image", image)

    time.sleep(args.delay)

try:
    cv2.destroyAllWindows()
except ValueError:
    print("Oops! It is not possible to get information from: {}", format(video_name))
